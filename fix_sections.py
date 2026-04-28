import os

filepath = r'd:\last smestet\ai based lab8\portfolio\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    new_lines.append(line)
    
    # After stack-cell container closing
    if "<!-- PROJECTS PAGE -->" in line:
        # Check if previous line is closing section
        if "</section>" not in lines[i-1] and "</section>" not in lines[i-2]:
            new_lines.insert(-1, "        </section>\n\n")
            
    # After projects container closing
    if "<!-- RESUME / DIGITAL CV PAGE -->" in line:
        if "</section>" not in lines[i-1] and "</section>" not in lines[i-2]:
            new_lines.insert(-1, "        </section>\n\n")

    # After resume container closing
    if "<!-- CONTACT MODAL -->" in line:
        if "</section>" not in lines[i-1] and "</section>" not in lines[i-2]:
            new_lines.insert(-1, "        </section>\n\n")

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Inserted missing </section> tags successfully!")
