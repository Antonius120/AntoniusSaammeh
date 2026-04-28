import re

html_path = r'd:\last smestet\ai based lab8\portfolio\index.html'
css_path = r'd:\last smestet\ai based lab8\portfolio\style.css'

# Update HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = html_content.replace('<div class="loader-logo">A</div>', '<div class="loader-logo">AS</div>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Update CSS
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

old_css = """.loader-logo {
    font-size: 4rem; font-weight: 800; color: transparent;
    -webkit-text-stroke: 2px rgba(255,255,255,0.1); position: relative;
    font-family: 'Inter', sans-serif; letter-spacing: -2px;
}
.loader-logo::before {
    content: 'A'; position: absolute; left: 0; top: 0;
    color: var(--blue); -webkit-text-stroke: 0px; width: 0%;
    overflow: hidden; animation: fillLogo 1.5s cubic-bezier(0.86, 0, 0.07, 1) forwards;
}
@keyframes fillLogo {
    0% { width: 0%; }
    100% { width: 100%; text-shadow: 0 0 20px rgba(59,130,246,0.6); }
}"""

new_css = """.loader-logo {
    font-size: 5rem; font-weight: 900; color: transparent;
    -webkit-text-stroke: 2px rgba(255,255,255,0.15); position: relative;
    font-family: 'Inter', sans-serif; letter-spacing: -4px;
}
.loader-logo::before {
    content: 'AS'; position: absolute; left: 0; top: 0;
    background: linear-gradient(135deg, #3b82f6, #f8fafc);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    -webkit-text-stroke: 0px; width: 0%; white-space: nowrap;
    overflow: hidden; animation: fillLogo 1.8s cubic-bezier(0.86, 0, 0.07, 1) forwards;
}
@keyframes fillLogo {
    0% { width: 0%; filter: drop-shadow(0 0 0px rgba(59,130,246,0)); }
    100% { width: 100%; filter: drop-shadow(0 0 25px rgba(59,130,246,0.8)); }
}"""

if old_css in css_content:
    css_content = css_content.replace(old_css, new_css)
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Updated preloader CSS successfully!")
else:
    print("Could not find the exact preloader CSS to replace.")
