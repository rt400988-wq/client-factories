import urllib.parse

# Batch C: Top 15 Real Estate Leads (Lucknow, Bhopal, Surat)
leads = [
    # LUCKNOW
    {"name": "Shalimar Corp Ltd.", "dm": "Khalid Masood", "phone": "915224030444"},
    {"name": "Rishita Developers", "dm": "Sudhir Kumar Agarwal", "phone": "915224077777"},
    {"name": "Eldeco Group", "dm": "Pankaj Bajaj", "phone": "915224039999"},
    {"name": "Omaxe Ltd.", "dm": "Mohit Goel", "phone": "915224055555"},
    {"name": "Paarth Infrabuild", "dm": "Pradeep Misra", "phone": "915224930000"},
    # BHOPAL
    {"name": "SAGE Realty", "dm": "Er. Sanjeev Agrawal", "phone": "919200700800"},
    {"name": "Amrit Homes", "dm": "Directors", "phone": "917770888880"},
    {"name": "Madhuban & Aashima Group", "dm": "Sanjay Badani", "phone": "919111811913"},
    {"name": "Agrawal Builders", "dm": "Agrawal Family Board", "phone": "917247765172"},
    {"name": "Prime Landmark Builders", "dm": "Management", "phone": "917024434754"},
    # SURAT
    {"name": "Sangini Group", "dm": "Velji Sheta", "phone": "919909926355"},
    {"name": "Happy Home Group", "dm": "Himmatbhai Patel", "phone": "912612205000"},
    {"name": "Avadh Group", "dm": "Dilipbhai", "phone": "919879364000"},
    {"name": "Rajgreen Group", "dm": "Jagdish Radadiya", "phone": "912612463333"},
    {"name": "Raghuvir Developers", "dm": "Dineshbhai Patel", "phone": "919638629131"}
]

html_content = """
<html>
<head>
    <title>Singularity Ops - Fast Outreach</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f2f5; padding: 20px; }
        .container { max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        h2 { text-align: center; color: #333; }
        .lead-card { border: 1px solid #ddd; padding: 15px; margin-bottom: 10px; border-radius: 8px; }
        .lead-name { font-size: 18px; font-weight: bold; color: #000; }
        .dm-name { color: #555; font-size: 14px; margin-bottom: 10px; }
        .wa-btn { display: block; background-color: #25D366; color: white; text-align: center; padding: 10px; text-decoration: none; border-radius: 5px; font-weight: bold; }
        .wa-btn:hover { background-color: #1ebe5d; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🚀 Batch C - Rapid Outreach</h2>
"""

for lead in leads:
    # Creating the highly-converting curiosity hook message
    message = f"Namaste {lead['dm']} ji & {lead['name']} Team! Main Saksham hu. Ek choti si cheez point out karni thi—aapke online ads aur Google profile se jo buyer traffic aa raha hai, usme 'Instant WhatsApp Funnel' missing hone ki wajah se weekly high-ticket inquiries drop ho rahi hain. Maine aapke brand ke liye ek 60-second speed-to-lead prototype design kiya hai. Agar aap allow karein, toh kya main uska 1-minute live demo link yahan share karu? It's completely free to check."

    # URL encoding the message for WhatsApp API
    encoded_message = urllib.parse.quote(message)
    wa_link = f"https://wa.me/{lead['phone']}?text={encoded_message}"

    html_content += f"""
        <div class="lead-card">
            <div class="lead-name">{lead['name']}</div>
            <div class="dm-name">Decision Maker: {lead['dm']}</div>
            <a href="{wa_link}" target="_blank" class="wa-btn">💬 Send Pitch to {lead['name']}</a>
        </div>
    """

html_content += """
    </div>
</body>
</html>
"""

# Save to an HTML file
with open("outreach_dashboard.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("✅ SUCCESS! 'outreach_dashboard.html' has been created. Open it in your browser to start tapping and sending!")
