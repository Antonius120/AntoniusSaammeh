import re

filepath = r'd:\last smestet\ai based lab8\portfolio\script.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_wheel = """    // ---- Scroll wheel navigation ----
    let accum = 0;
    let wheelTimer = null;
    document.addEventListener('wheel', (e) => {
        if (transitioning) return;
        e.preventDefault();
        accum += e.deltaY;
        if (wheelTimer) clearTimeout(wheelTimer);
        wheelTimer = setTimeout(() => { accum = 0; }, 250);

        const idx = pageOrder.indexOf(current);
        if (accum > 50 && idx < pageOrder.length - 1) {
            accum = 0; navigateTo(pageOrder[idx + 1]);
        } else if (accum < -50 && idx > 0) {
            accum = 0; navigateTo(pageOrder[idx - 1]);
        }
    }, { passive: false });"""

new_wheel = """    // ---- Scroll wheel navigation ----
    let accum = 0;
    let wheelTimer = null;
    document.addEventListener('wheel', (e) => {
        if (transitioning) return;
        
        const pageEl = document.getElementById('page-' + current);
        if (pageEl) {
            const atTop = pageEl.scrollTop <= 0;
            const atBottom = Math.ceil(pageEl.scrollTop + pageEl.clientHeight) >= pageEl.scrollHeight - 2;
            
            // Allow normal scrolling if not at boundaries
            if (e.deltaY > 0 && !atBottom) return;
            if (e.deltaY < 0 && !atTop) return;
        }

        e.preventDefault(); // prevent scroll bounce when navigating
        accum += e.deltaY;
        if (wheelTimer) clearTimeout(wheelTimer);
        wheelTimer = setTimeout(() => { accum = 0; }, 250);

        const idx = pageOrder.indexOf(current);
        if (accum > 50 && idx < pageOrder.length - 1) {
            accum = 0; navigateTo(pageOrder[idx + 1]);
        } else if (accum < -50 && idx > 0) {
            accum = 0; navigateTo(pageOrder[idx - 1]);
        }
    }, { passive: false });"""

old_touch = """    // ---- Touch swipe ----
    document.addEventListener('touchstart', (e) => { touchY = e.changedTouches[0].screenY; }, { passive: true });
    document.addEventListener('touchend', (e) => {
        if (transitioning) return;
        const diff = touchY - e.changedTouches[0].screenY;
        const idx = pageOrder.indexOf(current);
        if (Math.abs(diff) > 50) {
            if (diff > 0 && idx < pageOrder.length - 1) navigateTo(pageOrder[idx + 1]);
            else if (diff < 0 && idx > 0) navigateTo(pageOrder[idx - 1]);
        }
    }, { passive: true });"""

new_touch = """    // ---- Touch swipe ----
    document.addEventListener('touchstart', (e) => { touchY = e.changedTouches[0].screenY; }, { passive: true });
    document.addEventListener('touchend', (e) => {
        if (transitioning) return;
        const diff = touchY - e.changedTouches[0].screenY;
        
        const pageEl = document.getElementById('page-' + current);
        if (pageEl) {
            // Re-calculate since they might have scrolled during the swipe
            const atTop = pageEl.scrollTop <= 0;
            const atBottom = Math.ceil(pageEl.scrollTop + pageEl.clientHeight) >= pageEl.scrollHeight - 2;
            
            if (diff > 0 && !atBottom) return; // Swiping up (scrolling down), but not at bottom
            if (diff < 0 && !atTop) return; // Swiping down (scrolling up), but not at top
        }

        const idx = pageOrder.indexOf(current);
        if (Math.abs(diff) > 50) {
            if (diff > 0 && idx < pageOrder.length - 1) navigateTo(pageOrder[idx + 1]);
            else if (diff < 0 && idx > 0) navigateTo(pageOrder[idx - 1]);
        }
    }, { passive: true });"""

content = content.replace(old_wheel, new_wheel)
content = content.replace(old_touch, new_touch)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated scroll behavior successfully!")
