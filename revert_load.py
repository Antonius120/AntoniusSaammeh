import re

filepath = r'd:\last smestet\ai based lab8\portfolio\script.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# --- REVERT initialLoad ---
old_initial_load = """    // ---- Initial home page animation on load ----
    async function initialLoad() {
        // Skip the transition overlay typing for the very first load
        animatePageContent('home');

        // Hide preloader shortly after content starts animating
        setTimeout(() => {
            const preloader = document.getElementById('preloader');
            if (preloader) preloader.classList.add('hidden');
        }, 800);
    }"""

new_initial_load = """    // ---- Initial home page animation on load ----
    async function initialLoad() {
        transitioning = true;
        // Start black screen immediately
        await delay(300);
        await typeWriter(transitionText, 'Home', 80);
        await delay(400);
        
        // Slide up
        transitionOverlay.classList.add('hidden-top');
        animatePageContent('home');

        setTimeout(() => {
            transitionOverlay.style.transition = 'none';
            transitionOverlay.classList.remove('hidden-top');
            transitionOverlay.classList.add('hidden-bottom');
            transitionOverlay.offsetHeight;
            transitionOverlay.style.transition = '';
            transitioning = false;
        }, 700);
    }"""

# --- REVERT load event ---
old_load_event = """// Hook up audio and interactions on load
window.addEventListener('load', () => {
    // Initialize audio on first click anywhere
    document.body.addEventListener('click', initAudio, { once: true });"""

new_load_event = """// Hook up audio and interactions on load
window.addEventListener('load', () => {
    // Hide preloader
    setTimeout(() => {
        const preloader = document.getElementById('preloader');
        if (preloader) preloader.classList.add('hidden');
    }, 1600);

    // Initialize audio on first click anywhere
    document.body.addEventListener('click', initAudio, { once: true });"""

content = content.replace(old_initial_load, new_initial_load)
content = content.replace(old_load_event, new_load_event)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Reverted to original load sequence.")
