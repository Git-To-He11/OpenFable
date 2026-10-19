import os, json

base = r'C:\Users\Project Zero'
results = {}
for label, path in [('.agents/skills', '.agents/skills'), ('.codex/skills', '.codex/skills'),
                     ('.hermes/skills', '.hermes/skills'), ('.mimocode/skills', '.mimocode/skills'),
                     ('.zcode/skills', '.zcode/skills'), ('.openclaw/agents', '.openclaw/agents'),
                     ('.openclaw/extensions', '.openclaw/extensions'),
                     ('.openclaw/plugin-skills', '.openclaw/plugin-skills'),
                     ('.claude/skills', '.claude/skills'), ('.config/opencode/skills', '.config/opencode/skills')]:
    p = os.path.join(base, path)
    if os.path.isdir(p):
        items = sorted([x for x in os.listdir(p) if os.path.isdir(os.path.join(p, x))])
        results[label] = items
        print(f'{label}: {len(items)}')
    else:
        results[label] = []
        print(f'{label}: NOT FOUND')

all_skills = set()
for items in results.values():
    all_skills.update(items)
print(f'\nTotal unique skills across all local dirs: {len(all_skills)}')
for s in sorted(all_skills):
    present_in = [k for k, v in results.items() if s in v]
    if len(present_in) < 4:
        print(f'  MISSING: {s} -> {present_in}')
    elif len(present_in) == len([k for k,v in results.items() if v]):
        print(f'  IN_ALL: {s}')
