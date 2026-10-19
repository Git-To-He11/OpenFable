#!/usr/bin/env python3
import os

base = r'C:\Users\Project Zero'
dirs = [
    '.agents/skills', '.codex/skills', '.hermes/skills', 
    '.mimocode/skills', '.zcode/skills', '.claude/skills', 
    '.config/opencode/skills'
]
print("=== LOCAL SKILL COUNTS ===")
for d in dirs:
    p = os.path.join(base, d)
    if os.path.isdir(p):
        count = len([x for x in os.listdir(p) if os.path.isdir(os.path.join(p, x)) and not x.startswith('.')])
        print(f"  {d}: {count}")
    else:
        print(f"  {d}: NOT FOUND")

# Check openclaw
oc = os.path.join(base, '.openclaw')
if os.path.isdir(oc):
    for sub in ['agents', 'extensions', 'plugin-skills']:
        sp = os.path.join(oc, sub)
        if os.path.isdir(sp):
            items = [x for x in os.listdir(sp) if os.path.isdir(os.path.join(sp, x)) and not x.startswith('.')]
            print(f"  {sub}: {len(items)}")
