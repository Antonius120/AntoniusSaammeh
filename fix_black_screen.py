import re

filepath = r'd:\last smestet\ai based lab8\portfolio\script.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clear everything from the end of the Dock magnification logic (around line 430) to the end
content = re.sub(r'// ---- Dock magnification ----.*?$', '', content, flags=re.DOTALL)

# 2. Append the clean version of the final logic
final_logic = """// ---- Dock magnification ----
    const dock = document.getElementById('dock');
    const dockBtns = dock?.querySelectorAll('.dock-btn');
    if (dock && dockBtns) {
        dock.addEventListener('mousemove', (e) => {
            const rect = dock.getBoundingClientRect();
            const mx = e.clientX - rect.left;
            dockBtns.forEach(btn => {
                const br = btn.getBoundingClientRect();
                const center = br.left + br.width / 2 - rect.left;
                const dist = Math.abs(mx - center);
                if (dist < 100) {
                    const s = 1 + 0.2 * (1 - dist / 100);
                    const ty = -5 * (1 - dist / 100);
                    btn.style.transform = `scale(${s}) translateY(${ty}px)`;
                } else {
                    btn.style.transform = '';
                }
            });
        });
        dock.addEventListener('mouseleave', () => {
            dockBtns.forEach(b => b.style.transform = '');
        });
    }

    // ---- Initial home page animation on load ----
    async function initialLoad() {
        // Wait for preloader logo animation to almost finish
        await delay(3000);
        
        // Skip the transition overlay typing for the very first load
        animatePageContent('home');
        
        // Make sure the transition overlay is positioned at the bottom for next use
        if (transitionOverlay) {
            transitionOverlay.style.transition = 'none';
            transitionOverlay.classList.remove('hidden-top');
            transitionOverlay.classList.add('hidden-bottom');
            transitionOverlay.offsetHeight;
            transitionOverlay.style.transition = '';
        }
    }
    initialLoad();
});

// ======================================
// AUDIO MICRO-INTERACTIONS
// ======================================
const AudioContext = window.AudioContext || window.webkitAudioContext;
let audioCtx;

function initAudio() {
    if (!audioCtx) audioCtx = new AudioContext();
    if (audioCtx.state === 'suspended') audioCtx.resume();
}

function playHover() {
    if (!audioCtx) return;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(800, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(1200, audioCtx.currentTime + 0.05);
    gain.gain.setValueAtTime(0.01, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.05);
    osc.connect(gain); gain.connect(audioCtx.destination);
    osc.start(); osc.stop(audioCtx.currentTime + 0.05);
}

function playClick() {
    if (!audioCtx) return;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(400, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(100, audioCtx.currentTime + 0.1);
    gain.gain.setValueAtTime(0.05, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.1);
    osc.connect(gain); gain.connect(audioCtx.destination);
    osc.start(); osc.stop(audioCtx.currentTime + 0.1);
}

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
    document.body.addEventListener('click', initAudio, { once: true });

    // Add hover sounds to dock items, projects, tags, etc.
    const interactiveElements = document.querySelectorAll('.dock-item, .proj-card, .filter-tag, .sidebar-social, .slot-btn, button');
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', playHover);
        el.addEventListener('click', playClick);
    });
});
"""

content += final_logic

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Rewrote script.js correctly to fix the black screen issue.")
