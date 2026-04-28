import re

filepath = r'd:\last smestet\ai based lab8\portfolio\style.css'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the animation and styles to be even sharper and avoid filter-based blur
new_sharp_preloader_css = """@keyframes fillLogoNew {
    0% { clip-path: inset(0 100% 0 0); opacity: 0; }
    5% { opacity: 1; }
    100% { clip-path: inset(0 0 0 0); opacity: 1; }
}

.loader-logo {
    font-size: 7.5rem; font-weight: 900; 
    font-family: 'Inter', sans-serif;
    letter-spacing: -7px;
    position: relative;
    color: rgba(255,255,255,0.08); /* Sharper ghost text */
    line-height: 1;
    -webkit-font-smoothing: antialiased;
}

.loader-logo::after {
    content: 'AS';
    position: absolute; left: 0; top: 0;
    width: 100%;
    background: linear-gradient(135deg, #3b82f6, #ffffff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    clip-path: inset(0 100% 0 0);
    animation: fillLogoNew 3s cubic-bezier(0.86, 0, 0.07, 1) forwards;
    /* Use text-shadow instead of filter: drop-shadow to avoid blur during animation */
    text-shadow: 0 0 0px rgba(59,130,246,0);
    transition: text-shadow 0.5s ease 2.8s;
}

/* Add the glow ONLY at the very end using a separate class or late transition */
.loader-logo.loaded::after {
    text-shadow: 0 0 20px rgba(59,130,246,0.5);
}
"""

# Re-apply the preloader section with more robust sharpness
content = re.sub(r'@keyframes fillLogoNew {.*?filter: drop-shadow\(0 0 30px rgba\(59,130,246,0\.5\)\); \}', new_sharp_preloader_css, content, flags=re.DOTALL)
content = re.sub(r'\.loader-logo \{.*?\}', '', content, flags=re.DOTALL) # Clear old logo style

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Applied sharpness fix to Preloader.")
