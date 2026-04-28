// ======================================
// PORTFOLIO - Page Navigation + Typewriter
// ======================================

window.moveSlider = function(e, sliderId, direction) {
    e.stopPropagation(); // prevent clicking the card from navigating
    const slider = document.getElementById(sliderId);
    if (!slider) return;
    const imgs = slider.querySelectorAll('.slider-img');
    if (imgs.length === 0) return;
    
    let activeIdx = Array.from(imgs).findIndex(img => img.classList.contains('active'));
    if (activeIdx !== -1) imgs[activeIdx].classList.remove('active');
    else activeIdx = 0;
    
    let nextIdx = activeIdx + direction;
    if(nextIdx >= imgs.length) nextIdx = 0;
    if(nextIdx < 0) nextIdx = imgs.length - 1;
    
    imgs[nextIdx].classList.add('active');
};

window.openModal = function(src, isVideo = false) {
    const modal = document.getElementById('image-modal');
    const modalImg = document.getElementById('img-modal-target');
    const modalVideo = document.getElementById('video-modal-target');
    if(modal) {
        if(isVideo && modalVideo) {
            if(modalImg) modalImg.style.display = 'none';
            modalVideo.style.display = 'block';
            modalVideo.src = src;
            modalVideo.play();
        } else if (modalImg) {
            if(modalVideo) {
                modalVideo.style.display = 'none';
                modalVideo.pause();
            }
            modalImg.style.display = 'block';
            modalImg.src = src;
        }
        modal.classList.add('open');
    }
};

window.closeModal = function() {
    const modal = document.getElementById('image-modal');
    const modalVideo = document.getElementById('video-modal-target');
    if(modal) {
        modal.classList.remove('open');
        if (modalVideo) {
            modalVideo.pause();
            modalVideo.src = '';
        }
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const pageOrder = ['home', 'stack', 'projects', 'resume'];
    let current = 'home';
    let transitioning = false;
    let touchY = 0;
    
    document.body.setAttribute('data-page', current);

    // ---- Typewriter Effect ----
    function typeWriter(element, text, speed = 60) {
        return new Promise(resolve => {
            element.textContent = '';
            element.classList.remove('typed');
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
            let i = 0;
            function type() {
                if (i < text.length) {
                    element.textContent += text.charAt(i);
                    i++;
                    setTimeout(type, speed);
                } else {
                    element.classList.add('typed');
                    resolve();
                }
            }
            type();
        });
    }

    // Run typewriter on page headings & hand-text
    async function animatePageContent(pageId) {
        const page = document.getElementById('page-' + pageId);
        if (!page) return;

        // Get hand-text and heading
        const handText = page.querySelector('.hand-text');
        const heading = page.querySelector('.page-heading, .big-name');
        const animItems = page.querySelectorAll('.anim-item');

        // Reset all anim-items to hidden first
        animItems.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
        });

        // For home page, do special animation
        if (pageId === 'home') {
            const lines = page.querySelectorAll('.anim-item');
            for (let i = 0; i < lines.length; i++) {
                const el = lines[i];
                await delay(80);
                el.style.transition = 'opacity 0.5s, transform 0.5s';
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';

                // Typewriter for hand-text
                if (el.classList.contains('hand-text') && !el.classList.contains('sub-role')) {
                    const originalText = el.dataset.text || el.textContent;
                    el.dataset.text = originalText;
                    await typeWriter(el, originalText, 70);
                }
                // Typewriter for sub-role
                if (el.classList.contains('sub-role')) {
                    const originalText = el.dataset.text || el.textContent;
                    el.dataset.text = originalText;
                    await typeWriter(el, originalText, 40);
                }
            }
            return;
        }

        // For other pages: type the hand-text first, then heading, then content
        if (handText) {
            const originalHand = handText.dataset.text || handText.textContent;
            handText.dataset.text = originalHand;
            handText.style.opacity = '1';
            handText.style.transform = 'translateY(0)';
            await typeWriter(handText, originalHand, 60);
        }

        if (heading) {
            const originalHeading = heading.dataset.text || heading.textContent;
            heading.dataset.text = originalHeading;
            heading.style.opacity = '1';
            heading.style.transform = 'translateY(0)';
            await typeWriter(heading, originalHeading, 45);
        }

        await delay(100);

        // Then fade in the rest of the content items
        const restItems = page.querySelectorAll('.anim-item:not(.hand-text):not(.page-heading)');
        for (let i = 0; i < restItems.length; i++) {
            const el = restItems[i];
            if (el === handText || el === heading) continue;
            el.style.transition = `opacity 0.4s ${i * 0.08}s, transform 0.4s ${i * 0.08}s`;
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }
    }

    function delay(ms) { return new Promise(r => setTimeout(r, ms)); }

    const transitionOverlay = document.getElementById('pageTransition');
    const transitionText = document.getElementById('transitionText');

    // ---- Navigate function ----
    window.navigateTo = async function(to) {
        if (to === current || transitioning) return;
        transitioning = true;

        const pageName = to.charAt(0).toUpperCase() + to.slice(1);

        // Clear older text BEFORE sliding up
        transitionText.textContent = '';
        transitionText.classList.remove('typed');

        // 1. Slide up the overlay
        transitionOverlay.classList.remove('hidden-bottom');
        transitionOverlay.classList.remove('hidden-top');
        await delay(500); // Wait for overlay to cover the screen

        // 2. Type out page name on screen
        await typeWriter(transitionText, pageName, 80);
        await delay(400);

        // 3. Swap the active page behind the scenes
        const fromEl = document.getElementById('page-' + current);
        const toEl = document.getElementById('page-' + to);

        fromEl.classList.remove('active');
        toEl.classList.add('active');

        // Update dock
        document.querySelectorAll('.dock-btn[data-page]').forEach(b => {
            b.classList.toggle('active', b.dataset.page === to);
        });

        current = to;
        document.body.setAttribute('data-page', current);

        // 4. Slide up the overlay to reveal the new page
        transitionOverlay.classList.add('hidden-top');
        
        // 5. Trigger new page content animation
        animatePageContent(to);

        // 6. Reset overlay position silently
        setTimeout(() => {
            transitionOverlay.style.transition = 'none';
            transitionOverlay.classList.remove('hidden-top');
            transitionOverlay.classList.add('hidden-bottom');
            transitionOverlay.offsetHeight; // flush CSS
            transitionOverlay.style.transition = '';
            transitioning = false;
        }, 700);
    };

    // ---- Dock clicks ----
    document.querySelectorAll('.dock-btn[data-page]').forEach(btn => {
        btn.addEventListener('click', () => navigateTo(btn.dataset.page));
    });

    // ---- Theme Toggle ----
    const themeBtn = document.querySelector('.theme-btn');
    themeBtn.addEventListener('click', () => {
        const isLight = document.body.classList.toggle('light-mode');
        // Update SVG based on mode
        if (isLight) {
            themeBtn.innerHTML = `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>`;
            themeBtn.setAttribute('data-tooltip', 'Dark Mode');
        } else {
            themeBtn.innerHTML = `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>`;
            themeBtn.setAttribute('data-tooltip', 'Light Mode');
        }
    });

    // Helper to check if any modal is open
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
        if (transitioning || isModalOpen()) return;
        
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
    }, { passive: false });

    // ---- Keyboard ----
    document.addEventListener('keydown', (e) => {
        if (transitioning || isModalOpen()) return;
        const idx = pageOrder.indexOf(current);
        if ((e.key === 'ArrowDown' || e.key === 'ArrowRight') && idx < pageOrder.length - 1) {
            e.preventDefault(); navigateTo(pageOrder[idx + 1]);
        } else if ((e.key === 'ArrowUp' || e.key === 'ArrowLeft') && idx > 0) {
            e.preventDefault(); navigateTo(pageOrder[idx - 1]);
        }
    });

    // ---- Touch swipe ----
    document.addEventListener('touchstart', (e) => { touchY = e.changedTouches[0].screenY; }, { passive: true });
    document.addEventListener('touchend', (e) => {
        if (transitioning || isModalOpen()) return;
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
    }, { passive: true });

    // ---- Filter tags ----
    document.querySelectorAll('.filter-tag').forEach(tag => {
        tag.addEventListener('click', () => {
            document.querySelectorAll('.filter-tag').forEach(t => t.classList.remove('active'));
            tag.classList.add('active');
            const filter = tag.dataset.filter;
            document.querySelectorAll('.proj-card').forEach(card => {
                if (filter === 'all' || card.dataset.tags.includes(filter)) {
                    card.style.display = '';
                    card.style.animation = 'cardPop 0.3s ease both';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });

    // ---- Search ----
    const searchInput = document.getElementById('projectSearch');
    searchInput?.addEventListener('input', () => {
        const q = searchInput.value.toLowerCase();
        document.querySelectorAll('.proj-card').forEach(card => {
            const name = card.querySelector('.proj-name')?.textContent.toLowerCase() || '';
            const tags = card.dataset.tags || '';
            if (name.includes(q) || tags.includes(q)) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    });

    // ---- Contact Widget Logic ----
    const cwTabs = document.querySelectorAll('.cw-tab');
    const cwViews = document.querySelectorAll('.cw-view');

    cwTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            cwTabs.forEach(t => t.classList.remove('active'));
            cwViews.forEach(v => v.classList.remove('active'));
            
            tab.classList.add('active');
            document.getElementById('cw-' + tab.dataset.tab).classList.add('active');
        });
    });

    // ---- Calendar Logic ----
    const calMonthText = document.getElementById('calMonthText');
    const calGrid = document.getElementById('calGrid');
    const calPrevBtn = document.getElementById('calPrevBtn');
    const calNextBtn = document.getElementById('calNextBtn');
    
    let currentDate = new Date();
    let viewedDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1);
    let selectedDate = null;

    function renderCalendar() {
        if (!calGrid || !calMonthText) return;
        
        const year = viewedDate.getFullYear();
        const month = viewedDate.getMonth();
        
        const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        calMonthText.textContent = `${monthNames[month]} ${year}`;
        calGrid.innerHTML = '';
        
        const firstDay = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();
        
        const today = new Date();
        today.setHours(0,0,0,0);
        
        for (let i = 0; i < firstDay; i++) {
            const emptyBtn = document.createElement('button');
            emptyBtn.className = 'empty';
            emptyBtn.disabled = true;
            calGrid.appendChild(emptyBtn);
        }
        
        for (let i = 1; i <= daysInMonth; i++) {
            const btn = document.createElement('button');
            btn.textContent = i;
            
            const cellDate = new Date(year, month, i);
            cellDate.setHours(0,0,0,0);
            
            if (cellDate < today) {
                btn.disabled = true;
            } else {
                btn.addEventListener('click', () => {
                    calGrid.querySelectorAll('button').forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    selectedDate = cellDate;
                    
                    const slotBtns = document.querySelectorAll('.slot-btn');
                    slotBtns.forEach(b => b.classList.remove('active'));
                    const bookingForm = document.getElementById('bookingForm');
                    if (bookingForm) bookingForm.style.display = 'none';
                    const selectedTimeInput = document.getElementById('selectedTimeInput');
                    if (selectedTimeInput) selectedTimeInput.value = '';
                });
            }
            
            if (selectedDate && cellDate.getTime() === selectedDate.getTime()) {
                btn.classList.add('active');
            }
            calGrid.appendChild(btn);
        }
    }

    if (calPrevBtn) {
        calPrevBtn.addEventListener('click', () => {
            viewedDate.setMonth(viewedDate.getMonth() - 1);
            renderCalendar();
        });
    }
    if (calNextBtn) {
        calNextBtn.addEventListener('click', () => {
            viewedDate.setMonth(viewedDate.getMonth() + 1);
            renderCalendar();
        });
    }
    renderCalendar();

    // Time Slot Selection
    const slotBtns = document.querySelectorAll('.slot-btn');
    const bookingForm = document.getElementById('bookingForm');
    const selectedTimeInput = document.getElementById('selectedTimeInput');
    slotBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            slotBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            if (selectedTimeInput) selectedTimeInput.value = btn.innerText;
            if (bookingForm) bookingForm.style.display = 'flex';
        });
    });

    // ---- Form Handling ----
    const forms = [document.getElementById('contactForm'), document.getElementById('bookingForm')];
    forms.forEach(f => {
        if (!f) return;
        f.addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = f.querySelector('button[type="submit"]');
            const originalText = btn.innerHTML;
            btn.innerHTML = 'Processing...';
            btn.disabled = true;

            try {
                const formData = new FormData(f);
                
                // Build WhatsApp message
                let text = "New request from your Portfolio!\n\n";
                for (let [key, value] of formData.entries()) {
                    if (value && typeof value === 'string') {
                        text += `*${key.toUpperCase()}*: ${value}\n`;
                    }
                }
                if (f.id === 'bookingForm') {
                    const activeSlot = document.querySelector('.slot-btn.active');
                    if (activeSlot) text += `*SLOT*: ${activeSlot.textContent}\n`;
                }
                
                // Open WhatsApp using anchor tag click to bypass popup blockers
                const waUrl = `https://wa.me/201211445859?text=${encodeURIComponent(text)}`;
                const a = document.createElement('a');
                a.href = waUrl;
                a.target = '_blank';
                a.rel = 'noopener noreferrer';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);

                // Send email via FormSubmit
                const response = await fetch('https://formsubmit.co/ajax/samehtony017@gmail.com', {
                    method: 'POST',
                    headers: { 'Accept': 'application/json' },
                    body: formData
                });

                if (response.ok) {
                    btn.innerHTML = 'Success! ✓';
                    btn.style.background = '#10b981';
                } else {
                    throw new Error('Submission failed');
                }
            } catch (error) {
                console.error('Error:', error);
                btn.innerHTML = 'Error!';
                btn.style.background = '#ef4444';
            }

            setTimeout(() => {
                btn.innerHTML = originalText;
                btn.style.background = '';
                btn.disabled = false;
                f.reset();
            }, 3000);
        });
    });

    
// ---- Dock magnification ----
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
        // Transition overlay starts hidden via CSS, add class for JS consistency
        if (transitionOverlay) {
            transitionOverlay.classList.add('hidden-bottom');
        }

        // Wait for preloader logo animation to almost finish
        await delay(3000);
        
        // Skip the transition overlay typing for the very first load
        animatePageContent('home');
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
    // === TRIGGER PRELOADER ANIMATIONS ===
    // Adding .animate class via JS guarantees animations play
    // regardless of browser caching or load timing
    const animTargets = [
        '.loader-accent-line',
        '.loader-logo-wrap',
        '.loader-logo-curtain',
        '.loader-subtitle',
        '.loader-progress-wrap',
        '.loader-progress-bar',
        '.loader-progress-glow',
        '.loader-text'
    ];
    // Small delay to ensure DOM is painted first
    requestAnimationFrame(() => {
        animTargets.forEach(sel => {
            const el = document.querySelector(sel);
            if (el) el.classList.add('animate');
        });
    });

    // Animate the percentage counter
    const percentEl = document.getElementById('loaderPercent');
    if (percentEl) {
        let current = 0;
        const duration = 2600; // match progress bar duration
        const startDelay = 400; // match animation-delay
        const startTime = performance.now() + startDelay;
        
        function updatePercent(now) {
            const elapsed = now - startTime;
            if (elapsed < 0) { requestAnimationFrame(updatePercent); return; }
            const progress = Math.min(elapsed / duration, 1);
            // Use easing to match CSS cubic-bezier(0.4, 0, 0.2, 1)
            const eased = progress < 0.5 
                ? 4 * progress * progress * progress 
                : 1 - Math.pow(-2 * progress + 2, 3) / 2;
            current = Math.round(eased * 100);
            percentEl.textContent = current + '%';
            if (progress < 1) requestAnimationFrame(updatePercent);
        }
        requestAnimationFrame(updatePercent);
    }

    // Hide preloader after animation
    setTimeout(() => {
        const preloader = document.getElementById('preloader');
        if (preloader) {
            preloader.classList.add('hidden');
            setTimeout(() => { preloader.style.display = 'none'; }, 1200);
        }
    }, 3400);

    // Initialize audio on first click anywhere
    document.body.addEventListener('click', initAudio, { once: true });

    // Add hover sounds to dock items, projects, tags, etc.
    const interactiveElements = document.querySelectorAll('.dock-item, .proj-card, .filter-tag, .sidebar-social, .slot-btn, button');
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', playHover);
        el.addEventListener('click', playClick);
    });

    // === 3D TILT EFFECT FOR PHOTO FRAME ===
    const photoFrame = document.getElementById('photoFrame3D');
    if (photoFrame) {
        document.addEventListener('mousemove', (e) => {
            // Only apply effect if on home page
            if (current !== 'home') return;
            
            const xAxis = (window.innerWidth / 2 - e.pageX) / 25;
            const yAxis = (window.innerHeight / 2 - e.pageY) / 25;
            photoFrame.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
        });

        // Reset when mouse leaves window
        document.addEventListener('mouseleave', () => {
            if (current === 'home') {
                photoFrame.style.transform = `rotateY(0deg) rotateX(0deg)`;
            }
        });
    }
});
