#!/usr/bin/env python3
"""Consolidate all skills/plugins/extensions across all local platforms."""
import os, shutil

BASE = r'C:\Users\Project Zero'
TARGETS = [
    (os.path.join(BASE, '.agents', 'skills'), 'agents'),
    (os.path.join(BASE, '.codex', 'skills'), 'codex'),
    (os.path.join(BASE, '.hermes', 'skills'), 'hermes'),
    (os.path.join(BASE, '.mimocode', 'skills'), 'mimocode'),
    (os.path.join(BASE, '.zcode', 'skills'), 'zcode'),
    (os.path.join(BASE, '.claude', 'skills'), 'claude'),
    (os.path.join(BASE, '.config', 'opencode', 'skills'), 'opencode'),
]

def get_dir(path):
    return path

# Collect ALL unique skill names from all dirs (excluding hidden/.system/.hub)
all_names = set()
dir_contents = {}
for path, label in TARGETS:
    if os.path.isdir(path):
        items = sorted([x for x in os.listdir(path) 
                       if os.path.isdir(os.path.join(path, x)) 
                       and not x.startswith('.')])
        dir_contents[label] = items
        all_names.update(items)
    else:
        dir_contents[label] = []

print(f"Total unique skill names: {len(all_names)}")
print(f"Dirs found: {list(dir_contents.keys())}")

# Use .mimocode as primary source (largest local pool)
PRIMARY = os.path.join(BASE, '.mimocode', 'skills')

# For each target, copy missing skills
stats = {}
for target_path, target_label in TARGETS:
    if not os.path.isdir(target_path):
        os.makedirs(target_path, exist_ok=True)
    
    current = set([x for x in os.listdir(target_path) 
                   if os.path.isdir(os.path.join(target_path, x)) 
                   and not x.startswith('.')])
    missing = all_names - current
    
    copied = 0
    for name in sorted(missing):
        src = os.path.join(PRIMARY, name)
        if os.path.isdir(src):
            dst = os.path.join(target_path, name)
            if not os.path.isdir(dst):
                shutil.copytree(src, dst, dirs_exist_ok=True)
                copied += 1
            else:
                # Copy SKILL.md if missing in destination
                src_skill = os.path.join(src, 'SKILL.md')
                dst_skill = os.path.join(dst, 'SKILL.md')
                if os.path.exists(src_skill) and not os.path.exists(dst_skill):
                    shutil.copy2(src_skill, dst_skill)
                    copied += 1
    stats[target_label] = copied

print(f"\nConsolidation complete:")
for label, count in stats.items():
    print(f"  {label}: +{count} new skills")
