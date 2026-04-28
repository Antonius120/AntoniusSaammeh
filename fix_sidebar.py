import re

filepath = r'd:\last smestet\ai based lab8\portfolio\style.css'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_css = """/* ======================================
   RIGHT SOCIAL SIDEBAR
   ====================================== */
.social-sidebar{
    position:fixed;right:28px;top:50%;transform:translateY(-50%);z-index:90;
    display:flex;flex-direction:column;gap:16px;
    animation:sideIn 0.4s 0.4s ease both;
}
.sidebar-social{
    width:40px;height:40px;display:flex;align-items:center;justify-content:center;
    border:1px solid var(--border);border-radius:12px;color:var(--text-3);
    transition:all 0.3s;
}
.sidebar-social:hover{color:var(--text);border-color:rgba(255,255,255,0.2);transform:scale(1.1)}"""

new_css = """/* ======================================
   RIGHT SOCIAL SIDEBAR
   ====================================== */
.social-sidebar{
    position:fixed;right:28px;top:50%;transform:translateY(-50%);z-index:90;
    display:flex;flex-direction:column;gap:16px;align-items:center;
    animation:sideIn 0.4s 0.4s ease both;
}
.social-sidebar::before, .social-sidebar::after {
    content:''; width:1px; height:40px; background:rgba(255,255,255,0.15);
}
.sidebar-social{
    width:44px;height:44px;display:flex;align-items:center;justify-content:center;
    border:1px solid rgba(255,255,255,0.08);border-radius:14px;color:rgba(255,255,255,0.4);
    transition:all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    position:relative;
    text-decoration: none;
}
.sidebar-social svg {
    width: 20px; height: 20px; transition: all 0.3s;
}
.sidebar-social:hover{
    background:#fff; color:#000; border-color:#fff; transform:scale(1.1);
}
.sidebar-social::before {
    content: attr(aria-label);
    position: absolute; right: calc(100% + 12px); top: 50%;
    transform: translateY(-50%) translateX(10px) scale(0.9);
    background: #fff; color: #000; font-size: 0.75rem; font-weight: 700;
    padding: 6px 12px; border-radius: 20px;
    opacity: 0; visibility: hidden; pointer-events: none; white-space: nowrap;
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.sidebar-social:hover::before {
    opacity: 1; visibility: visible; transform: translateY(-50%) translateX(0) scale(1);
}"""

content = content.replace(old_css, new_css)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated sidebar CSS!")
