import re

filepath = r'd:\last smestet\ai based lab8\portfolio\style.css'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the problematic preloader block with a clean, robust one
new_preloader_css = """/* ======================================
   PRELOADER
   ====================================== */
#preloader {
    position: fixed; inset: 0; z-index: 9999;
    background: #0a0a0c;
    display: flex; align-items: center; justify-content: center;
    transition: opacity 0.8s ease, visibility 0.8s ease;
}
#preloader.hidden { opacity: 0; visibility: hidden; pointer-events: none; }

.preloader-content { 
    display: flex; flex-direction: column; align-items: center; gap: 24px; 
}

.loader-logo {
    font-size: 7rem; font-weight: 900; 
    font-family: 'Inter', sans-serif;
    letter-spacing: -7px;
    position: relative;
    color: rgba(255,255,255,0.03);
    line-height: 1;
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
}

@keyframes fillLogoNew {
    0% { clip-path: inset(0 100% 0 0); }
    100% { clip-path: inset(0 0 0 0); filter: drop-shadow(0 0 30px rgba(59,130,246,0.5)); }
}

.loader-text {
    font-size: 0.9rem; color: #64748b; 
    letter-spacing: 0.5em; text-transform: uppercase;
    opacity: 0;
    animation: fadeInText 1s 0.8s forwards, pulseText 2s infinite;
}
@keyframes fadeInText { to { opacity: 1; } }
@keyframes pulseText { 0%, 100% { opacity: 0.4; } 50% { opacity: 1; } }
"""

# Find the old block and replace it
content = re.sub(r'/\* =+ \s+ PRELOADER \s+ =+ \*/.*?@keyframes pulseText { 0%, 100% { opacity: 0\.3; } 50% { opacity: 1; } }', new_preloader_css, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Cleaned up and upgraded Preloader CSS.")
