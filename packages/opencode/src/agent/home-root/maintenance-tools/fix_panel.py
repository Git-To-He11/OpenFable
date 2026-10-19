import os

base = r'C:\Users\Project Zero\FreeAI_AI-Inference-Workstation\docs'
path = os.path.join(base, 'index.html')
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Replace "Launching Europe Summer" with FreeAI-appropriate text
c = c.replace('Launching Europe Summer', 'v1.2.0 — Autonomous SDLC Agents')

# 2. Remove applivery icon class
c = c.replace('iconify iconify--applivery', 'inline-svg')

# 3. Fix panel note text
c = c.replace(
    'Fully integrated \u2014 works with the Applivery workspace you already run',
    'Fully integrated \u2014 works with the stack you already run'
)

# 4. Replace panel CTA buttons with styled links
old_btn1 = '<button type="button" class="btn btn--inverse" data-v-f3beba39="">Get early access'
new_btn1 = '<a href="#install" class="btn btn--primary" data-v-f3beba39="" style="height:36px;padding:0 16px;font-size:13px;">Get Started</a>'
c = c.replace(old_btn1, new_btn1)

old_btn2 = '<button type="button" class="btn btn--ghost-dark" data-v-f3beba39="">Talk to a specialist</button></div>'
new_btn2 = '<a href="deploy.html" class="btn btn--ghost" data-v-f3beba39="" style="height:36px;padding:0 16px;font-size:13px;">Learn More</a></div>'
c = c.replace(old_btn2, new_btn2)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print('Panel fixed.')
