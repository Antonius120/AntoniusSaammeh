import re

with open(r'd:\last smestet\ai based lab8\portfolio\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the boundaries to replace
# From: <!-- RESUME PAGE -->
# To: the end of <!-- DIGITAL CV MODAL --> </div> </div> </div>

start_marker = "        <!-- RESUME PAGE -->\n        <section class=\"page\" id=\"page-resume\">"
end_marker = '<!-- CONTACT PAGE -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # Backtrack end_idx to include any whitespace before <!-- CONTACT PAGE -->
    end_idx = content.rfind('        <!-- CONTACT PAGE -->', 0, end_idx + 1)
    
    new_section = """        <!-- RESUME / DIGITAL CV PAGE -->
        <section class="page" id="page-resume">
            <div class="page-inner" style="max-width:850px;">
                <div class="cv-container-inline anim-item" style="--d:0.1s">
                    <div class="cv-top-bar">
                        <div class="cv-top-left">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
                            <span>Digital CV</span>
                        </div>
                    </div>

                    <div class="cv-body">
                        <h1 class="cv-name">ANTONIUS <span>SAMEH</span></h1>
                        <p class="cv-title">AI / ML ENGINEER & FULL-STACK DEVELOPER</p>
                        <div class="cv-contact-row">
                            <span>📧 samehtony017@gmail.com</span>
                            <span>📍 Alexandria, Egypt</span>
                        </div>

                        <div class="cv-columns">
                            <!-- LEFT COLUMN -->
                            <div class="cv-left">
                                <h4 class="cv-section-title">OVERVIEW</h4>
                                <p class="cv-text">AI/ML Engineer & Full-Stack Developer with 3+ years of experience delivering 11+ projects spanning deep learning, computer vision, recommender systems, .NET platforms, and n8n workflow automation. Specialized in building production-grade intelligent systems.</p>

                                <h4 class="cv-section-title">PROJECTS</h4>
                                <div class="cv-projects-list">
                                    <span class="cv-proj">PLANT DISEASE DETECTION</span>
                                    <span class="cv-proj">PLS E-COMMERCE & LOGISTICS</span>
                                    <span class="cv-proj">AI-DRIVEN ACADEMIC ADVISING</span>
                                    <span class="cv-proj">YOLO ATTENDANCE SYSTEM</span>
                                    <span class="cv-proj">AI GAMES (WUMPUS/PACMAN)</span>
                                    <span class="cv-proj">DATA WAREHOUSE ETL</span>
                                </div>

                                <h4 class="cv-section-title">EXPERIENCE</h4>
                                <div class="cv-edu-item">
                                    <div class="cv-edu-info">
                                        <strong>Freelance AI/ML Engineer</strong>
                                        <p>Self-Employed · 11+ projects</p>
                                    </div>
                                    <span class="cv-edu-year">2022 — NOW</span>
                                </div>
                                <div class="cv-edu-item">
                                    <div class="cv-edu-info">
                                        <strong>Software Dev Intern</strong>
                                        <p>Petrochemicals Logistic Services (PLS)</p>
                                    </div>
                                    <span class="cv-edu-year">2025</span>
                                </div>
                                <div class="cv-edu-item">
                                    <div class="cv-edu-info">
                                        <strong>Java Intern</strong>
                                        <p>Information Technology Institute (ITI)</p>
                                    </div>
                                    <span class="cv-edu-year">2023</span>
                                </div>

                                <h4 class="cv-section-title">ACADEMIC BACKGROUND</h4>
                                <div class="cv-edu-item">
                                    <div class="cv-edu-info">
                                        <strong>B.Sc. Computer Science (AI Track)</strong>
                                        <p>Alamein International University</p>
                                    </div>
                                    <span class="cv-edu-year">2022 — 2026</span>
                                </div>
                            </div>

                            <!-- RIGHT COLUMN -->
                            <div class="cv-right">
                                <h4 class="cv-section-title">STACK</h4>
                                <div class="cv-stack-pills">
                                    <span>Python</span><span>TensorFlow</span><span>PyTorch</span>
                                    <span>ASP.NET</span><span>Blazor</span><span>React</span>
                                    <span>Java</span><span>C++</span><span>SQL</span>
                                    <span>n8n</span><span>SignalR</span><span>Docker</span>
                                </div>

                                <h4 class="cv-section-title">IMPACT</h4>
                                <p class="cv-text">
                                    Delivered <strong>11+ projects</strong> across AI & web.<br>
                                    Built <strong>real-time logistics platform</strong> at PLS.<br>
                                    AI sales forecasting with <strong>95% accuracy</strong>.<br>
                                    Published <strong>research paper</strong> on AI advising.
                                </p>

                                <h4 class="cv-section-title">CONNECT</h4>
                                <div class="cv-connect-links">
                                    <a href="https://www.linkedin.com/in/antonius-sameh" target="_blank">
                                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                                        LinkedIn
                                    </a>
                                    <a href="https://github.com/antonius-sameh" target="_blank">
                                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
                                        GitHub
                                    </a>
                                </div>
                            </div>
                        </div>

                        <!-- Footer -->
                        <div class="cv-footer">
                            <p>ENGLISH (PROF.) · ARABIC (NATIVE)</p>
                            <p class="cv-footer-sub">ENGINEERED WITH PRECISION</p>
                            <p class="cv-footer-sub">© 2026 ANTONIUS SAMEH</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""
    
    new_content = content[:start_idx] + new_section + content[end_idx:]
    with open(r'd:\last smestet\ai based lab8\portfolio\index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced successfully!")
else:
    print(f"Could not find markers. start: {start_idx}, end: {end_idx}")
