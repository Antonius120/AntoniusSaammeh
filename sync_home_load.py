import re

filepath = r'd:\last smestet\ai based lab8\portfolio\script.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the standalone initialLoad definition and call from DOMContentLoaded
content = re.sub(r'// ---- Initial home page animation on load ----.*?initialLoad\(\);', '', content, flags=re.DOTALL)

# 2. Add it into the window.load listener for perfect synchronization
new_load_logic = """// Hook up audio and interactions on load
window.addEventListener('load', () => {
    // Hide preloader after its animation (3s) finishes
    setTimeout(() => {
        const preloader = document.getElementById('preloader');
        if (preloader) {
            preloader.classList.add('hidden');
            
            // START HOME PAGE ANIMATION EXACTLY AS PRELOADER HIDES
            if (typeof animatePageContent === 'function') {
                animatePageContent('home');
            }

            // Force removal of preloader from DOM after fade
            setTimeout(() => { preloader.style.display = 'none'; }, 800);
        }
    }, 3000);"""

content = re.sub(r'// Hook up audio and interactions on load.*?setTimeout\(\(\) => \{', new_load_logic, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Synchronized Home animation with Preloader hiding.")
