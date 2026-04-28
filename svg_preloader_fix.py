import re

html_path = r'd:\last smestet\ai based lab8\portfolio\index.html'
css_path = r'd:\last smestet\ai based lab8\portfolio\style.css'

# --- SVG VERSION OF PRELOADER ---
svg_preloader_html = """    <div id="preloader">
        <div class="preloader-content">
            <svg class="loader-svg" viewBox="0 0 400 150">
                <defs>
                    <linearGradient id="logoGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#3b82f6" />
                        <stop offset="100%" stop-color="#ffffff" />
                    </linearGradient>
                    <clipPath id="logoClip">
                        <rect id="clipRect" x="0" y="0" width="0" height="150" />
                    </clipPath>
                </defs>
                <!-- Ghost Background -->
                <text x="50%" y="50%" text-anchor="middle" dominant-baseline="middle" class="svg-text-ghost">AS</text>
                <!-- Animated Fill -->
                <text x="50%" y="50%" text-anchor="middle" dominant-baseline="middle" class="svg-text-fill" clip-path="url(#logoClip)">AS</text>
            </svg>
            <div class="loader-text">Loading Experience...</div>
        </div>
    </div>
"""

# --- CSS FOR SVG PRELOADER ---
svg_preloader_css = """/* ======================================
   PRELOADER (SVG VERSION)
   ====================================== */
#preloader {
    position: fixed; inset: 0; z-index: 9999;
    background: #0a0a0c;
    display: flex; align-items: center; justify-content: center;
    transition: opacity 0.8s ease, visibility 0.8s ease;
}
#preloader.hidden { opacity: 0; visibility: hidden; pointer-events: none; }

.preloader-content { 
    display: flex; flex-direction: column; align-items: center; gap: 10px;
    width: 100%; max-width: 500px;
}

.loader-svg {
    width: 100%; height: auto;
    max-height: 200px;
}

.svg-text-ghost {
    font-family: 'Inter', sans-serif;
    font-weight: 900; font-size: 120px;
    fill: rgba(255,255,255,0.05);
    letter-spacing: -5px;
}

.svg-text-fill {
    font-family: 'Inter', sans-serif;
    font-weight: 900; font-size: 120px;
    fill: url(#logoGradient);
    letter-spacing: -5px;
}

#clipRect {
    animation: fillSVG 3s cubic-bezier(0.86, 0, 0.07, 1) forwards;
}

@keyframes fillSVG {
    0% { width: 0; }
    100% { width: 400; }
}

.loader-text {
    font-size: 0.9rem; color: #64748b; 
    letter-spacing: 0.5em; text-transform: uppercase;
    animation: pulseText 2s infinite;
}
@keyframes pulseText { 0%, 100% { opacity: 0.4; } 50% { opacity: 1; } }
"""

# Update HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()
html_content = re.sub(r'<!-- ====== PRELOADER ====== -->.*?</div>\s+</div>', '<!-- ====== PRELOADER ====== -->\n' + svg_preloader_html, html_content, flags=re.DOTALL)
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Update CSS
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()
# Replace preloader section
css_content = re.sub(r'/\* =+ \s+ PRELOADER.*?DOCK LOGO & DIVIDER', svg_preloader_css + '\n\n/* ======================================\n   DOCK LOGO & DIVIDER', css_content, flags=re.DOTALL)
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Switched to SVG Preloader for 100% sharpness.")
