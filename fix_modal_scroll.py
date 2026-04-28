import re

filepath = r'd:\last smestet\ai based lab8\portfolio\script.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_wheel_start = """    // ---- Scroll wheel navigation ----
    let accum = 0;
    let wheelTimer = null;
    document.addEventListener('wheel', (e) => {
        if (transitioning) return;"""

new_wheel_start = """    // Helper to check if any modal is open
    function isModalOpen() {
        const contactModal = document.getElementById('contactModal');
        const imageModal = document.getElementById('image-modal');
        if (contactModal && contactModal.classList.contains('open')) return true;
        if (imageModal && imageModal.classList.contains('open')) return true;
        return false;
    }

    // ---- Scroll wheel navigation ----
    let accum = 0;
    let wheelTimer = null;
    document.addEventListener('wheel', (e) => {
        if (transitioning || isModalOpen()) return;"""

old_keydown_start = """    // ---- Keyboard ----
    document.addEventListener('keydown', (e) => {
        if (transitioning) return;"""

new_keydown_start = """    // ---- Keyboard ----
    document.addEventListener('keydown', (e) => {
        if (transitioning || isModalOpen()) return;"""

old_touchend_start = """    // ---- Touch swipe ----
    document.addEventListener('touchstart', (e) => { touchY = e.changedTouches[0].screenY; }, { passive: true });
    document.addEventListener('touchend', (e) => {
        if (transitioning) return;"""

new_touchend_start = """    // ---- Touch swipe ----
    document.addEventListener('touchstart', (e) => { touchY = e.changedTouches[0].screenY; }, { passive: true });
    document.addEventListener('touchend', (e) => {
        if (transitioning || isModalOpen()) return;"""

content = content.replace(old_wheel_start, new_wheel_start)
content = content.replace(old_keydown_start, new_keydown_start)
content = content.replace(old_touchend_start, new_touchend_start)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated modal scroll behavior successfully!")
