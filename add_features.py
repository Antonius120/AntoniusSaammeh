import re

css_path = r'd:\last smestet\ai based lab8\portfolio\style.css'
js_path = r'd:\last smestet\ai based lab8\portfolio\script.js'

# --- UPDATE CSS ---
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

preloader_css = """
/* ======================================
   PRELOADER
   ====================================== */
#preloader {
    position: fixed; inset: 0; z-index: 9999;
    background: rgba(10, 10, 12, 0.8);
    backdrop-filter: blur(25px); -webkit-backdrop-filter: blur(25px);
    display: flex; align-items: center; justify-content: center;
    transition: opacity 0.8s ease, visibility 0.8s ease;
}
#preloader.hidden { opacity: 0; visibility: hidden; }
.preloader-content { display: flex; flex-direction: column; align-items: center; gap: 20px; }
.loader-logo {
    font-size: 4rem; font-weight: 800; color: transparent;
    -webkit-text-stroke: 2px rgba(255,255,255,0.1); position: relative;
    font-family: 'Inter', sans-serif; letter-spacing: -2px;
}
.loader-logo::before {
    content: 'A'; position: absolute; left: 0; top: 0;
    color: var(--blue); -webkit-text-stroke: 0px; width: 0%;
    overflow: hidden; animation: fillLogo 1.5s cubic-bezier(0.86, 0, 0.07, 1) forwards;
}
@keyframes fillLogo {
    0% { width: 0%; }
    100% { width: 100%; text-shadow: 0 0 20px rgba(59,130,246,0.6); }
}
.loader-text {
    font-size: 0.8rem; color: var(--text-3); letter-spacing: 0.3em;
    text-transform: uppercase; animation: pulseText 1.5s infinite;
}
@keyframes pulseText { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; } }
"""
if "#preloader" not in css_content:
    css_content += preloader_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

# --- UPDATE JS ---
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

audio_js = """
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
    // Hide preloader
    setTimeout(() => {
        const preloader = document.getElementById('preloader');
        if (preloader) preloader.classList.add('hidden');
    }, 1600);

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

if "initAudio" not in js_content:
    js_content += audio_js
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)

print("Updated CSS and JS!")
