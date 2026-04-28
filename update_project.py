import re

filepath = r'd:\last smestet\ai based lab8\portfolio\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace YOLO project card
old_proj = """                    <div class="proj-card" data-tags="ai,python">
                        <div class="proj-thumb" style="background:linear-gradient(135deg,#1a1025,#2d1b4e,#3d2568)">
                            <div class="proj-tech-tags">
                                <span class="tech-tag tag-blue">Python</span>
                                <span class="tech-tag tag-red">YOLO</span>
                                <span class="tech-more">+2 More</span>
                            </div>
                            <div class="proj-thumb-inner"><span>👤</span></div>
                        </div>
                        <h3 class="proj-name">YOLO Attendance System</h3>
                        <p class="proj-desc">Real-time face verification using One-Shot Learning</p>
                    </div>"""

new_proj = """                    <div class="proj-card" data-tags="ai,python">
                        <div class="proj-thumb" style="background:#111; position:relative;">
                            <video src="linkedin_video.mp4" autoplay loop muted playsinline style="position:absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; opacity:0.6; transition:opacity 0.3s;"></video>
                            <div class="proj-tech-tags" style="z-index: 2; position:relative;">
                                <span class="tech-tag tag-blue">Python</span>
                                <span class="tech-tag tag-green" style="background:rgba(16,185,129,0.1);color:#10b981;border-color:rgba(16,185,129,0.2);">Streamlit</span>
                                <span class="tech-more">+5 More</span>
                            </div>
                            <div class="proj-thumb-inner" style="z-index: 2; position:relative; opacity:0; width:100%; height:100%; display:flex; align-items:center; justify-content:center; transition:opacity 0.3s;" onmouseover="this.previousElementSibling.previousElementSibling.style.opacity='1'" onmouseout="this.previousElementSibling.previousElementSibling.style.opacity='0.6'">
                                <span style="font-size:1.5rem; background:rgba(0,0,0,0.5); padding:10px; border-radius:50%;">▶</span>
                            </div>
                        </div>
                        <h3 class="proj-name">CityWise: Smart Transportation Optimization</h3>
                        <p class="proj-desc">Tackling urban mobility using real-time data, graph algorithms (Dijkstra, A*), and interactive visualizations.</p>
                    </div>"""

if old_proj in content:
    content = content.replace(old_proj, new_proj)
else:
    print("Could not find the YOLO proj-card string exactly. Trying regex or manual replacement.")
    # Fallback to a simpler replace
    content = content.replace('<h3 class="proj-name">YOLO Attendance System</h3>', '<h3 class="proj-name">CityWise: Smart Transportation Optimization</h3>')
    content = content.replace('<p class="proj-desc">Real-time face verification using One-Shot Learning</p>', '<p class="proj-desc">Tackling urban mobility using real-time data, graph algorithms (Dijkstra, A*), and interactive visualizations.</p>')


# Replace YOLO in resume
content = content.replace('<span class="cv-proj">YOLO ATTENDANCE SYSTEM</span>', '<span class="cv-proj">CITYWISE: TRANSPORTATION OPTIMIZATION</span>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated YOLO to CityWise successfully!")
