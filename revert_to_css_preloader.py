import re

html_path = r'd:\last smestet\ai based lab8\portfolio\index.html'
css_path = r'd:\last smestet\ai based lab8\portfolio\style.css'
js_path = r'd:\last smestet\ai based lab8\portfolio\script.js'

# --- RESTORE CSS PRELOADER HTML ---
new_html = """    <div id="preloader">
        <div class="preloader-content">
            <div class="loader-logo">AS</div>
            <div class="loader-text">Loading Experience...</div>
        </div>
    </div>
"""
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()
html_content = re.sub(r'<!-- ====== PRELOADER ====== -->.*?</div>\s+</div>', '<!-- ====== PRELOADER ====== -->\n' + new_html, html_content, flags=re.DOTALL)
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# --- RESTORE CSS PRELOADER STYLES (WITH BLUR) ---
new_css = """/* ======================================
   PRELOADER
   ====================================== */
#preloader {
    position: fixed; inset: 0; z-index: 9999;
    background: rgba(10, 10, 12, 0.8);
    backdrop-filter: blur(25px); -webkit-backdrop-filter: blur(25px);
    display: flex; align-items: center; justify-content: center;
    transition: opacity 0.8s ease, visibility 0.8s ease;
}
#preloader.hidden { 
    opacity: 0; 
    visibility: hidden; 
    pointer-events: none;
    backdrop-filter: blur(0px);
    -webkit-backdrop-filter: blur(0px);
}
.preloader-content { display: flex; flex-direction: column; align-items: center; gap: 20px; }
.loader-logo {
    font-size: 5rem; font-weight: 900; color: transparent;
    -webkit-text-stroke: 2px rgba(255,255,255,0.15); position: relative;
    font-family: 'Inter', sans-serif; letter-spacing: -4px;
}
.loader-logo::before {
    content: 'AS'; position: absolute; left: 0; top: 0;
    background: linear-gradient(135deg, #3b82f6, #f8fafc);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    -webkit-text-stroke: 0px; width: 0%; white-space: nowrap;
    overflow: hidden; animation: fillLogo 3s cubic-bezier(0.86, 0, 0.07, 1) forwards;
}
@keyframes fillLogo {
    0% { width: 0%; filter: drop-shadow(0 0 0px rgba(59,130,246,0)); }
    100% { width: 100%; filter: drop-shadow(0 0 20px rgba(59,130,246,0.5)); }
}
.loader-text {
    font-size: 0.8rem; color: var(--text-3); letter-spacing: 0.3em;
    text-transform: uppercase; animation: pulseText 1.5s infinite;
}
@keyframes pulseText { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; } }
"""
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()
css_content = re.sub(r'/\* =+ \s+ PRELOADER.*?DOCK LOGO & DIVIDER', new_css + '\n\n/* ======================================\n   DOCK LOGO & DIVIDER', css_content, flags=re.DOTALL)
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

# --- RESTORE JS SYNC LOGIC ---
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Ensure we have the initialLoad function back and the load listener hides the preloader
# and triggers the animation properly.
new_js_logic = """    // ---- Initial home page animation on load ----
    async function initialLoad() {
        // Wait for preloader logo animation to almost finish
        await delay(3000);
        
        // Skip the transition overlay typing for the very first load
        animatePageContent('home');
        
        // Make sure the transition overlay is positioned at the bottom for next use
        transitionOverlay.style.transition = 'none';
        transitionOverlay.classList.remove('hidden-top');
        transitionOverlay.classList.add('hidden-bottom');
        transitionOverlay.offsetHeight;
        transitionOverlay.style.transition = '';
    }
    initialLoad();
});

// Hook up audio and interactions on load
window.addEventListener('load', () => {
    // Hide preloader after animation
    setTimeout(() => {
        const preloader = document.getElementById('preloader');
        if (preloader) {
            preloader.classList.add('hidden');
            setTimeout(() => { preloader.style.display = 'none'; }, 800);
        }
    }, 3200);

    // Initialize audio on first click anywhere
    document.body.addEventListener('click', initAudio, { once: true });"""

# This is a bit complex to regex replace perfectly, so I'll do a simple find/replace on the end block
js_content = re.sub(r'// ---- Initial home page animation on load ----.*?initialLoad\(\);', '', js_content, flags=re.DOTALL)
js_content = re.sub(r'// Hook up audio and interactions on load.*?document\.body\.addEventListener', new_js_logic, js_content, flags=re.DOTALL)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Reverted to the requested CSS preloader state with perfect sync.")
