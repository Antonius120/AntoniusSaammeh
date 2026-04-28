import re

filepath = r'd:\last smestet\ai based lab8\portfolio\script.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_code = """            try {
                const formData = new FormData(f);
                const response = await fetch('https://formsubmit.co/ajax/samehtony017@gmail.com', {
                    method: 'POST',
                    headers: { 'Accept': 'application/json' },
                    body: formData
                });"""

new_code = """            try {
                const formData = new FormData(f);
                
                // Build WhatsApp message
                let text = "New request from your Portfolio!\\n\\n";
                for (let [key, value] of formData.entries()) {
                    if (value && typeof value === 'string') {
                        text += `*${key.toUpperCase()}*: ${value}\\n`;
                    }
                }
                if (f.id === 'bookingForm') {
                    const activeSlot = document.querySelector('.slot-btn.active');
                    if (activeSlot) text += `*SLOT*: ${activeSlot.textContent}\\n`;
                }
                
                // Open WhatsApp immediately
                window.open(`https://wa.me/201211445859?text=${encodeURIComponent(text)}`, '_blank');

                // Send email via FormSubmit
                const response = await fetch('https://formsubmit.co/ajax/samehtony017@gmail.com', {
                    method: 'POST',
                    headers: { 'Accept': 'application/json' },
                    body: formData
                });"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("WhatsApp integration added successfully!")
else:
    print("Could not find the target code block to replace.")
