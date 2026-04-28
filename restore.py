import re

with open(r'd:\last smestet\ai based lab8\portfolio\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

contact_page_html = """
        <!-- CONTACT PAGE -->
        <section class="page" id="page-contact">
            <div class="page-inner" style="max-width: 850px; padding-top: 20px;">
                <div class="contact-widget anim-item" style="--d:0.1s">
                    
                    <!-- Header -->
                    <div class="cw-header">
                        <h2><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg> Contact Me</h2>
                    </div>
                    
                    <!-- Tabs -->
                    <div class="cw-tabs">
                        <button class="cw-tab active" data-tab="book">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg> Book a Call
                        </button>
                        <button class="cw-tab" data-tab="message">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg> Message
                        </button>
                    </div>

                    <div class="cw-body">
                        <!-- BOOK A CALL VIEW -->
                        <div class="cw-view active" id="cw-book">
                            <div class="booking-grid">
                                
                                <!-- Left: Calendar -->
                                <div class="booking-cal">
                                    <div class="cal-head">
                                        <h3>April 2026</h3>
                                        <div class="cal-nav">
                                            <button>&lt;</button>
                                            <button>&gt;</button>
                                        </div>
                                    </div>
                                    <div class="cal-days-header">
                                        <span>Su</span><span>Mo</span><span>Tu</span><span>We</span><span>Th</span><span>Fr</span><span>Sa</span>
                                    </div>
                                    <div class="cal-grid">
                                        <span class="cal-day empty"></span><span class="cal-day empty"></span>
                                        <span class="cal-day">1</span><span class="cal-day">2</span><span class="cal-day">3</span><span class="cal-day">4</span><span class="cal-day">5</span>
                                        <span class="cal-day">6</span><span class="cal-day">7</span><span class="cal-day">8</span><span class="cal-day">9</span><span class="cal-day">10</span><span class="cal-day">11</span><span class="cal-day">12</span>
                                        <span class="cal-day">13</span><span class="cal-day">14</span><span class="cal-day active">15</span><span class="cal-day">16</span><span class="cal-day">17</span><span class="cal-day">18</span><span class="cal-day">19</span>
                                        <span class="cal-day">20</span><span class="cal-day">21</span><span class="cal-day">22</span><span class="cal-day">23</span><span class="cal-day">24</span><span class="cal-day">25</span><span class="cal-day">26</span>
                                        <span class="cal-day">27</span><span class="cal-day">28</span><span class="cal-day">29</span><span class="cal-day">30</span>
                                    </div>
                                </div>
                                
                                <!-- Right: Booking Form -->
                                <div class="booking-form">
                                    <form class="msg-form" id="bookingForm">
                                        <div class="f-group">
                                            <label>Name *</label>
                                            <input type="text" name="name" placeholder="Your Name" required>
                                        </div>
                                        <div class="f-group">
                                            <label>Email *</label>
                                            <input type="email" name="email" placeholder="Your Email" required>
                                        </div>
                                        <div class="f-group">
                                            <label>Reason *</label>
                                            <textarea name="reason" placeholder="What's this meeting for?" rows="3" required></textarea>
                                        </div>
                                        <button type="submit" class="submit-pill">Confirm Booking</button>
                                    </form>
                                </div>
                            </div>
                        </div>

                        <!-- MESSAGE VIEW -->
                        <div class="cw-view" id="cw-message">
                            <!-- We wrap the form tightly to match screenshot widths -->
                            <form class="msg-form" id="contactForm" style="max-width: 500px; margin: 0 auto; padding: 20px 0;">
                                <div class="f-group">
                                    <label>Email *</label>
                                    <div class="input-icon">
                                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                                        <input type="email" name="email" placeholder="name@example.com" required>
                                    </div>
                                </div>
                                <div class="f-group">
                                    <label>Phone Number *</label>
                                    <div class="input-icon">
                                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                                        <input type="tel" name="phone" placeholder="+1 (555) 123-4567" required>
                                    </div>
                                </div>
                                <div class="whatsapp-toggle">
                                    <span>
                                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg> 
                                        WhatsApp Available
                                    </span>
                                    <label class="switch">
                                        <input type="checkbox" name="whatsapp_available">
                                        <span class="slider round"></span>
                                    </label>
                                </div>
                                <div class="f-group">
                                    <label>Message *</label>
                                    <textarea name="message" placeholder="How can I help you?" rows="5" required></textarea>
                                </div>
                                <button type="submit" class="submit-pill" style="margin-top:20px;">Send Message</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>"""

if "<!-- CONTACT PAGE -->" not in content:
    with open(r'd:\last smestet\ai based lab8\portfolio\index.html', 'w', encoding='utf-8') as f:
        f.write(content.rstrip() + '\n\n' + contact_page_html)
    print("Appended Contact page and missing tags!")
else:
    print("Contact page already exists!")
