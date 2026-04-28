import re

with open(r'd:\last smestet\ai based lab8\portfolio\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the start of the contact page
old_start = """        <!-- CONTACT PAGE -->
        <section class="page" id="page-contact">
            <div class="page-inner" style="max-width: 850px; padding-top: 20px;">
                <div class="contact-widget anim-item" style="--d:0.1s">
                    
                    <!-- Header -->
                    <div class="cw-header">
                        <h2><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg> Contact Me</h2>
                    </div>"""

new_start = """        <!-- CONTACT MODAL -->
        <div class="contact-modal" id="contactModal">
            <div class="contact-widget">
                
                <!-- Header -->
                <div class="cw-header">
                    <h2><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg> Contact Me</h2>
                    <button class="cw-close" onclick="document.getElementById('contactModal').classList.remove('open')">&times;</button>
                </div>"""

# Replace the end of the contact page
old_end = """                </div>
            </div>
        </section>"""

new_end = """            </div>
        </div>"""

if old_start in content and old_end in content:
    content = content.replace(old_start, new_start)
    content = content.replace(old_end, new_end)
    with open(r'd:\last smestet\ai based lab8\portfolio\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced HTML structure successfully!")
else:
    print("Could not find start or end tags")
