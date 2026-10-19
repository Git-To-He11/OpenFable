import os, shutil

BASE = r'C:\Users\Project Zero'
OC_AGENTS = os.path.join(BASE, 'oc_agents_extracted', 'agents')
TARGETS = [
    os.path.join(BASE, '.agents', 'agents'),
    os.path.join(BASE, '.claude', 'agents'),
    os.path.join(BASE, '.hermes', 'agents'),
    os.path.join(BASE, '.mimocode', 'agents'),
    os.path.join(BASE, '.zcode', 'agents'),
]

if not os.path.isdir(OC_AGENTS):
    print(f"Source not found: {OC_AGENTS}")
    exit(1)

for target in TARGETS:
    os.makedirs(target, exist_ok=True)
    count = 0
    for item in os.listdir(OC_AGENTS):
        src = os.path.join(OC_AGENTS, item)
        dst = os.path.join(target, item)
        if os.path.isdir(src) and not os.path.isdir(dst):
            shutil.copytree(src, dst)
            count += 1
    total = len([x for x in os.listdir(target) if os.path.isdir(os.path.join(target, x))])
    print(f"  {os.path.basename(os.path.dirname(target))}/agents: {total} total (+{count} new)")

# Cleanup
shutil.rmtree(os.path.join(BASE, 'oc_agents_extracted'), ignore_errors=True)
oc_tar = os.path.join(BASE, 'oc_agents.tar.gz')
if os.path.exists(oc_tar):
    os.remove(oc_tar)
print("Done. Cleaned up temp files.")
