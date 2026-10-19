import os, shutil
BASE = r'C:\Users\Project Zero'
oc_src = os.path.join(BASE, '.openclaw')
targets = ['.agents', '.claude', '.hermes', '.mimocode', '.zcode']

for t in targets:
    td = os.path.join(BASE, t)
    # plugin-skills -> skills
    ps_src = os.path.join(oc_src, 'plugin-skills')
    if os.path.isdir(ps_src):
        dst = os.path.join(td, 'skills')
        os.makedirs(dst, exist_ok=True)
        count = 0
        for item in os.listdir(ps_src):
            si = os.path.join(ps_src, item)
            di = os.path.join(dst, item)
            if os.path.isdir(si) and not os.path.isdir(di):
                shutil.copytree(si, di)
                count += 1
        print(f'plugin-skills -> {t}: +{count}')
    # extensions
    ext_src = os.path.join(oc_src, 'extensions')
    if os.path.isdir(ext_src):
        dst = os.path.join(td, 'extensions')
        os.makedirs(dst, exist_ok=True)
        count = 0
        for item in os.listdir(ext_src):
            si = os.path.join(ext_src, item)
            di = os.path.join(dst, item)
            if os.path.isdir(si) and not os.path.isdir(di):
                shutil.copytree(si, di)
                count += 1
        print(f'extensions -> {t}: +{count}')
    # agents
    ag_src = os.path.join(oc_src, 'agents')
    if os.path.isdir(ag_src):
        dst = os.path.join(td, 'agents')
        os.makedirs(dst, exist_ok=True)
        count = 0
        for item in os.listdir(ag_src):
            si = os.path.join(ag_src, item)
            di = os.path.join(dst, item)
            if os.path.isdir(si) and not os.path.isdir(di):
                shutil.copytree(si, di)
                count += 1
        print(f'agents -> {t}: +{count}')

print('Local openclaw sync done.')