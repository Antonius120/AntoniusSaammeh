import re

html_path = r'd:\last smestet\ai based lab8\portfolio\index.html'
css_path = r'd:\last smestet\ai based lab8\portfolio\style.css'

# --- UPDATE HTML ---
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

old_dock_start = """    <!-- ====== BOTTOM DOCK NAV ====== -->
    <nav class="dock" id="dock">
        <button class="dock-btn active" data-page="home" data-tooltip="Home">"""

new_dock_start = """    <!-- ====== BOTTOM DOCK NAV ====== -->
    <nav class="dock" id="dock">
        <!-- Premium AS Logo -->
        <button class="dock-logo dock-btn" data-page="home" data-tooltip="Antonius Sameh">
            <div class="logo-inner">
                <span class="logo-a">A</span><span class="logo-s">S</span>
            </div>
        </button>
        <div class="dock-divider"></div>

        <button class="dock-btn active" data-page="home" data-tooltip="Home">"""

if old_dock_start in html_content:
    html_content = html_content.replace(old_dock_start, new_dock_start)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Added Logo to HTML")
else:
    print("Could not find dock start in HTML.")

# --- UPDATE CSS ---
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

logo_css = """
/* ======================================
   DOCK LOGO & DIVIDER
   ====================================== */
.dock-logo {
    width: 48px !important; height: 48px !important;
    border-radius: 14px;
    background: linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.01));
    border: 1px solid rgba(255,255,255,0.15) !important;
    display: flex; align-items: center; justify-content: center;
    position: relative;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.2);
    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
    margin-right: 4px;
}
.logo-inner {
    font-family: 'Inter', sans-serif;
    font-weight: 900;
    font-size: 1.3rem;
    letter-spacing: -1.5px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #ffffff, #94a3b8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5));
    transition: all 0.4s;
}
.logo-a { 
    background: linear-gradient(135deg, #3b82f6, #60a5fa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.logo-s { margin-left: 0.5px; }

.dock-logo:hover {
    transform: translateY(-8px) scale(1.15) !important;
    border-color: rgba(255,255,255,0.4) !important;
    box-shadow: 0 10px 25px rgba(59,130,246,0.4), inset 0 1px 0 rgba(255,255,255,0.4) !important;
    background: linear-gradient(135deg, rgba(255,255,255,0.15), rgba(255,255,255,0.05));
}
.dock-logo:hover .logo-inner {
    transform: scale(1.05);
}
.dock-divider {
    width: 1px; height: 28px;
    background: rgba(255,255,255,0.12);
    margin: 0 6px;
    border-radius: 1px;
}
"""

if ".dock-logo" not in css_content:
    css_content += logo_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Added Logo to CSS")
