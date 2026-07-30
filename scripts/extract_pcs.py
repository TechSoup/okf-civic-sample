#!/usr/bin/env python3
"""Vendor a minimal, attributed snapshot of the Candid PCS codes this bundle uses.

The full Philanthropy Classification System is published by Candid as a
spreadsheet. This repo does not ship that file: it extracts only the codes its
own records actually reference — code, facet, title, and Candid's scope note —
into `_shared/pcs/pcs-codes.json`, so `build_hubs.py` and `validate.py` run
offline with no external dependency.

    python3 scripts/extract_pcs.py /path/to/PCS_Taxonomy_Definitions_2024.xlsx

The Philanthropy Classification System is (c) Candid, made available under
CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
Source: https://taxonomy.candid.org
"""
import glob
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, '_shared', 'pcs', 'pcs-codes.json')
NS = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
NSMAP = {'m': NS[1:-1]}

# Worksheet name -> the facet name this profile uses for it.
FACETS = {'Subject': 'subject', 'Population': 'population', 'OrgType': 'org_type'}

ATTRIBUTION = {
    'vocabulary': 'Candid Philanthropy Classification System (PCS)',
    'edition': '2024 taxonomy definitions',
    'rights_holder': 'Candid',
    'license': 'CC BY 4.0',
    'license_url': 'https://creativecommons.org/licenses/by/4.0/',
    'source': 'https://taxonomy.candid.org',
    'note': ('Extracted subset. Only the codes referenced by this bundle are included; '
             'titles and scope notes are Candid\'s, unmodified. No codes were invented, '
             'renamed, or altered.'),
}


def read_sheets(path):
    z = zipfile.ZipFile(path)
    shared = []
    if 'xl/sharedStrings.xml' in z.namelist():
        sst = ET.fromstring(z.read('xl/sharedStrings.xml'))
        shared = [''.join(t.text or '' for t in si.iter(NS + 't'))
                  for si in sst.findall('m:si', NSMAP)]
    wb = ET.fromstring(z.read('xl/workbook.xml'))
    rels = ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
    rid_to_target = {r.get('Id'): r.get('Target') for r in rels}
    RID = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'

    out = {}
    for sh in wb.findall('.//m:sheet', NSMAP):
        name = sh.get('name')
        if name not in FACETS:
            continue
        target = rid_to_target[sh.get(RID)].lstrip('/')
        if not target.startswith('xl/'):
            target = 'xl/' + target
        rows = []
        tree = ET.fromstring(z.read(target))
        for r in tree.findall('.//m:row', NSMAP):
            cells = []
            for c in r.findall('m:c', NSMAP):
                v = c.find('m:v', NSMAP)
                if v is None:
                    cells.append('')
                elif c.get('t') == 's':
                    cells.append(shared[int(v.text)])
                else:
                    cells.append(v.text)
            while len(cells) < 9:
                cells.append('')
            rows.append([x.strip() for x in cells])
        out[FACETS[name]] = rows
    return out


def codes_in_use():
    """Every PCS code referenced by any record in this repo."""
    used = set()
    pat = re.compile(r'\b([SPE][A-Z]\d{6})\b')
    for p in glob.glob(os.path.join(ROOT, '**', '*.md'), recursive=True):
        if '/venv/' in p:
            continue
        used.update(pat.findall(open(p, encoding='utf-8').read()))
    return used


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    if not os.path.exists(src):
        sys.exit(f'not found: {src}')

    sheets = read_sheets(src)
    used = codes_in_use()
    entries, missing = {}, set(used)

    for facet, rows in sheets.items():
        header = rows[0]
        try:
            note_col = header.index('Definitions and Scope Notes')
        except ValueError:
            note_col = 7
        for r in rows[1:]:
            code = r[0]
            if code not in used:
                continue
            labels = [x for x in r[2:6] if x]
            note = r[note_col] if note_col < len(r) else ''
            # In this workbook the scope note is appended after the label chain.
            if note and note in labels:
                note = ''
            entries[code] = {
                'code': code,
                'facet': facet,
                'title': labels[-1] if labels else code,
                'path': labels,
                'former_ntee': r[1] if r[1] and r[1] != 'NEW' else None,
                'scope_note': note or None,
            }
            missing.discard(code)

    if missing:
        print(f'WARNING: {len(missing)} referenced code(s) not found in the taxonomy:')
        for m in sorted(missing):
            print('  -', m)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    payload = {'attribution': ATTRIBUTION,
               'codes': {k: entries[k] for k in sorted(entries)}}
    with open(OUT, 'w', encoding='utf-8') as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write('\n')

    by = {}
    for e in entries.values():
        by[e['facet']] = by.get(e['facet'], 0) + 1
    print(f'wrote {os.path.relpath(OUT, ROOT)} — {len(entries)} codes ' +
          ', '.join(f'{v} {k}' for k, v in sorted(by.items())))
    return 1 if missing else 0


if __name__ == '__main__':
    sys.exit(main())
