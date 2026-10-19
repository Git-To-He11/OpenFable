import os, tarfile, io, subprocess, shutil

REMOTE = 'root@93.188.162.144'
LOCAL_BASE = r'C:\Users\Project Zero'
OC_AGENTS = os.path.join(LOCAL_BASE, '.openclaw', 'agents')
TARGETS = [
    os.path.join(LOCAL_BASE, '.agents', 'agents'),
    os.path.join(LOCAL_BASE, '.claude', 'agents'),
    os.path.join(LOCAL_BASE, '.hermes', 'agents'),
    os.path.join(LOCAL_BASE, '.mimocode', 'agents'),
    os.path.join(LOCAL_BASE, '.zcode', 'agents'),
]

# List all agent dirs on remote
result = subprocess.run(
    ['ssh', REMOTE, 'ls ~/.openclaw/agents/'],
    capture_output=True, text=True
)
agents = [a for a in result.stdout.strip().split('\n') if a]
print(f'Found {len(agents)} agents on remote')

# Download each agent via tar+scp in batches
batch_size = 20
for batch_start in range(0, len(agents), batch_size):
    batch = agents[batch_start:batch_start+batch_size]
    # Create tar on remote
    tar_name = f'/tmp/batch_{batch_start//batch_size}.tar.gz'
    agent_args = ' '.join(batch)
    subprocess.run(
        ['ssh', REMOTE, f'tar czf {tar_name} -C ~/.openclaw/agents {agent_args}'],
        capture_output=True
    )
    # SCP to local
    local_tar = os.path.join(LOCAL_BASE, f'batch_{batch_start//batch_size}.tar.gz')
    subprocess.run(
        ['scp', f'{REMOTE}:{tar_name}', local_tar],
        capture_output=True
    )
    # Extract
    with tarfile.open(local_tar, 'r:gz') as tar:
        tar.extractall(path=OC_AGENTS)
    os.remove(local_tar)
    subprocess.run(['ssh', REMOTE, f'rm -f {tar_name}'], capture_output=True)
    print(f'  Downloaded batch {batch_start//batch_size + 1}: {len(batch)} agents')

print(f'Total agents downloaded: {len(agents)}')

# Now copy to all target platforms
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
    print(f'  {os.path.basename(os.path.dirname(target))}/agents: {total} total (+{count} new)')

print('Done.')
