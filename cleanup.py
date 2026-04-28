with open(r'd:\last smestet\ai based lab8\portfolio\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx1 = content.find('cv-footer-sub')
section_end = content.find('</section>', idx1)
section_end = content.find('\n', section_end) + 1
contact_start = content.find('        <!-- CONTACT PAGE -->')

if section_end > 0 and contact_start > section_end:
    new_content = content[:section_end] + '\n' + content[contact_start:]
    with open(r'd:\last smestet\ai based lab8\portfolio\index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Done! Cleaned up orphaned content.")
else:
    print("Could not find markers.")
