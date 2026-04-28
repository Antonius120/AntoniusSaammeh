import re

filepath = r'd:\last smestet\ai based lab8\portfolio\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

preloader_html = """<body>
    <!-- ====== PRELOADER ====== -->
    <div id="preloader">
        <div class="preloader-content">
            <div class="loader-logo">A</div>
            <div class="loader-text">Loading Experience...</div>
        </div>
    </div>
"""

content = content.replace('<body>', preloader_html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Added preloader HTML!")
