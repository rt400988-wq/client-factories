import urllib.parse

# Batch C: 15 Real Estate Titans (Lucknow, Bhopal, Surat)
leads = [
    {"id": "LKO-1", "name": "Shalimar Corp Ltd.", "dm": "Khalid Masood / Kunal Seth", "phone": "915224030444", "city": "Lucknow"},
    {"id": "LKO-2", "name": "Rishita Developers", "dm": "Sudhir Kumar Agarwal", "phone": "915224077777", "city": "Lucknow"},
    {"id": "LKO-3", "name": "Eldeco Group", "dm": "Pankaj Bajaj", "phone": "915224039999", "city": "Lucknow"},
    {"id": "LKO-4", "name": "Omaxe Ltd.", "dm": "Mohit Goel", "phone": "915224055555", "city": "Lucknow"},
    {"id": "LKO-5", "name": "Paarth Infrabuild", "dm": "Pradeep Misra", "phone": "915224930000", "city": "Lucknow"},
    {"id": "BHO-1", "name": "SAGE Realty", "dm": "Er. Sanjeev Agrawal", "phone": "919200700800", "city": "Bhopal"},
    {"id": "BHO-2", "name": "Amrit Homes", "dm": "Directors", "phone": "917770888880", "city": "Bhopal"},
    {"id": "BHO-3", "name": "Madhuban & Aashima Group", "dm": "Sanjay Badani", "phone": "919111811913", "city": "Bhopal"},
    {"id": "BHO-4", "name": "Agrawal Builders", "dm": "Agrawal Family Board", "phone": "917247765172", "city": "Bhopal"},
    {"id": "BHO-5", "name": "Prime Landmark Builders", "dm": "Management", "phone": "917024434754", "city": "Bhopal"},
    {"id": "ST-1", "name": "Sangini Group", "dm": "Velji Sheta / Sanjay Patel", "phone": "919909926355", "city": "Surat"},
    {"id": "ST-2", "name": "Happy Home Group", "dm": "Himmatbhai Patel", "phone": "912612205000", "city": "Surat"},
    {"id": "ST-3", "name": "Avadh Group", "dm": "Dilipbhai / Lavjibhai", "phone": "919879364000", "city": "Surat"},
    {"id": "ST-4", "name": "Rajgreen Group", "dm": "Jagdish Radadiya", "phone": "912612463333", "city": "Surat"},
    {"id": "ST-5", "name": "Raghuvir Developers", "dm": "Dineshbhai Patel", "phone": "919638629131", "city": "Surat"}
]

# The Permission-Based Curiosity Hook
raw_message = (
    "Namaste {dm} & Team {name}!\n\n"
    "Main Saksham hu. Ek choti si cheez point out karni thi—aapke online ads aur Google profile se jo buyer traffic aa raha hai, "
    "usme 'Instant WhatsApp Funnel' missing hone ki wajah se weekly high-ticket inquiries drop ho rahi hain.\n\n"
    "Maine aapke brand ke liye ek 60-second speed-to-lead prototype design kiya hai. "
    "Agar aap allow karein, toh kya main uska 1-minute live demo link yahan share karu? It’s completely free to check."
)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Striker Dashboard - Batch C</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 20px; }
        .container { max-width: 1000px; margin: auto; }
        .header { text-align: center; margin-bottom: 30px; }
        .header h1 { color: #38bdf8; font-size: 2.5em; margin-bottom: 5px; }
        .header p { color: #94a3b8; font-size: 1.1em; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
        .card { background-color: #1e293b; padding: 20px; border-radius: 12px; border-left: 5px solid #10b981; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
        .card h3 { margin: 0 0 10px 0; color: #f1f5f9; font-size: 1.2em; }
        .card p { margin: 5px 0; color: #cbd5e1; font-size: 0.9em; }
        .btn { display: inline-block; width: 100%; text-align: center; margin-top: 15px; padding: 12px 0; background-color: #10b981; color: white; text-decoration: none; border-radius: 6px; font-weight: bold; transition: background 0.3s; box-sizing: border-box; }
        .btn:hover { background-color: #059669; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Singularity Ops - Striker Dashboard</h1>
            <p>Batch C: Real Estate Titans (High-Ticket 1-Tap Outreach)</p>
        </div>
        <div class="grid">
"""

for lead in leads:
    # Format the message for this specific lead
    personalized_msg = raw_message.format(dm=lead["dm"], name=lead["name"])
    encoded_msg = urllib.parse.quote(personalized_msg)
    
    # Generate WhatsApp Link
    wa_link = f"https://api.whatsapp.com/send?phone={lead['phone']}&text={encoded_msg}"
    
    html_content += f"""
            <div class="card">
                <h3>{lead['name']}</h3>
                <p><strong>City:</strong> {lead['city']}</p>
                <p><strong>DM:</strong> {lead['dm']}</p>
                <a href="{wa_link}" target="_blank" class="btn">💬 1-Tap WhatsApp Pitch</a>
            </div>
    """

html_content += """
        </div>
    </div>
</body>
</html>
"""

# Save to HTML file
with open("Batch_C_Dashboard.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("✅ BOOM! Batch_C_Dashboard.html has been generated successfully. Open it in your browser to start firing!")
