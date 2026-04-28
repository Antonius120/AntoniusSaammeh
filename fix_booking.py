import re

filepath = r'd:\last smestet\ai based lab8\portfolio\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace spans in calendar with buttons
old_cal = """                                    <div class="cal-grid">
                                        <span class="cal-day empty"></span><span class="cal-day empty"></span>
                                        <span class="cal-day">1</span><span class="cal-day">2</span><span class="cal-day">3</span><span class="cal-day">4</span><span class="cal-day">5</span>
                                        <span class="cal-day">6</span><span class="cal-day">7</span><span class="cal-day">8</span><span class="cal-day">9</span><span class="cal-day">10</span><span class="cal-day">11</span><span class="cal-day">12</span>
                                        <span class="cal-day">13</span><span class="cal-day">14</span><span class="cal-day active">15</span><span class="cal-day">16</span><span class="cal-day">17</span><span class="cal-day">18</span><span class="cal-day">19</span>
                                        <span class="cal-day">20</span><span class="cal-day">21</span><span class="cal-day">22</span><span class="cal-day">23</span><span class="cal-day">24</span><span class="cal-day">25</span><span class="cal-day">26</span>
                                        <span class="cal-day">27</span><span class="cal-day">28</span><span class="cal-day">29</span><span class="cal-day">30</span>
                                    </div>"""

new_cal = """                                    <div class="cal-grid">
                                        <button class="empty" disabled></button><button class="empty" disabled></button>
                                        <button disabled>1</button><button disabled>2</button><button disabled>3</button><button disabled>4</button>
                                        <button disabled>5</button><button disabled>6</button><button disabled>7</button><button disabled>8</button>
                                        <button disabled>9</button><button disabled>10</button><button disabled>11</button><button disabled>12</button>
                                        <button disabled>13</button><button disabled>14</button><button disabled>15</button><button disabled>16</button>
                                        <button disabled>17</button><button disabled>18</button><button disabled>19</button><button disabled>20</button>
                                        <button disabled>21</button><button class="active">22</button><button>23</button><button>24</button>
                                        <button>25</button><button>26</button><button>27</button><button>28</button>
                                        <button>29</button><button>30</button>
                                    </div>"""

content = content.replace(old_cal, new_cal)

# Replace the booking form
old_form = """                                <!-- Right: Booking Form -->
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
                                </div>"""

new_form = """                                <!-- Right: Booking Details -->
                                <div class="booking-details">
                                    <div class="bd-group" style="padding-bottom: 12px; border-bottom: none;">
                                        <div class="bd-title" style="margin-bottom: 16px; font-size: 0.8rem; color: #fff;">WEDNESDAY, APRIL 22</div>
                                        <div style="padding: 30px 20px; text-align: center; border-radius: 12px; border: 1px solid var(--border); background: rgba(255,255,255,0.02); color: var(--text-2); font-size: 0.85rem; font-style: italic;">
                                            No meetings scheduled.
                                        </div>
                                    </div>

                                    <div class="bd-group" style="padding-bottom: 12px; border-bottom: none;">
                                        <div class="timezone-picker">
                                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>
                                            <span style="margin-left:6px;">User Timezone</span> <span class="info-icon" style="cursor:help; margin-left:4px; font-size:0.75rem; color:var(--text-3);">ⓘ</span>
                                        </div>
                                        <div class="tz-select">
                                            <span>UTC+02:00 (EET)</span>
                                            <span>&gt;</span>
                                        </div>
                                    </div>

                                    <div class="bd-group" style="border-bottom: none;">
                                        <div class="timezone-picker" style="font-size: 1.05rem; color: #fff; font-weight: 700; gap: 6px; margin-bottom: 16px;">
                                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                                            Available Slots
                                        </div>
                                        <div class="slots-grid" style="grid-template-columns: repeat(4, 1fr);">
                                            <button class="slot-btn">09:00 AM</button>
                                            <button class="slot-btn">10:00 AM</button>
                                            <button class="slot-btn">11:00 AM</button>
                                            <button class="slot-btn">12:00 PM</button>
                                            <button class="slot-btn">02:00 PM</button>
                                            <button class="slot-btn">03:00 PM</button>
                                            <button class="slot-btn">04:00 PM</button>
                                            <button class="slot-btn">05:00 PM</button>
                                        </div>
                                    </div>
                                    
                                    <div class="bd-group" style="border-bottom: none; padding-top: 10px;">
                                        <div class="f-group">
                                            <label style="font-size:0.85rem; font-weight:700;">Name * <span class="info-icon" style="cursor:help; font-weight:400; color:var(--text-3);">ⓘ</span></label>
                                            <input type="text" name="name" style="background: rgba(255,255,255,0.03); border-color: rgba(255,255,255,0.1); padding: 14px; border-radius: 12px; margin-top: 4px; width: 100%; color: white;">
                                        </div>
                                    </div>
                                </div>"""

content = content.replace(old_form, new_form)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated right column successfully!")
