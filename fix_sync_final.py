import re

filepath = r'd:\last smestet\ai based lab8\portfolio\script.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Clean up the broken window.load part
new_load_logic = """// Hook up audio and interactions on load
window.addEventListener('load', () => {
    // Hide preloader after its animation (3s) finishes
    setTimeout(() => {
        const preloader = document.getElementById('preloader');
        if (preloader) {
            preloader.classList.add('hidden');
            
            // Trigger Home Animation exactly as preloader hides
            if (typeof animatePageContent === 'function') {
                animatePageContent('home');
            }

            // Force removal of preloader from DOM after fade
            setTimeout(() => { preloader.style.display = 'none'; }, 800);
        }
    }, 3000);

    // Initialize audio on first click anywhere
    document.body.addEventListener('click', initAudio, { once: true });"""

# Remove the messy part from the end of the file
content = re.sub(r'// Hook up audio and interactions on load.*?document\.body\.addEventListener', new_load_logic, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed script.js syntax and restored perfect synchronization.")
