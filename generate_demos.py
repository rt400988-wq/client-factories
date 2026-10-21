import pandas as pd
import urllib.parse

# 1. Load your newly generated Top 100 Leads file
df = pd.read_csv('Top_100_Dashboard_Leads.csv')

# The "Curiosity Hook" 
raw_message = (
    "Namaste {dm} & Team {name}!\n\n"
    "Main Saksham hu. Ek choti si detail notice ki thi—aapke Google Maps aur online profile se jo local inquiries aa rahi hain, "
    "usme instant 'WhatsApp Booking Funnel' missing hone se weekly clients/patients drop ho rahe hain.\n\n"
    "Maine specially aapke brand ke liye ek 60-second WhatsApp booking prototype banaya hai. "
    "Agar aap allow karein, toh kya main 1-minute live demo link share karu? It’s completely free to check!"
)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Striker Dashboard - TOP 100</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 20px; }
        .container { max-width: 1200px; margin: auto; }
        .header { text-align: center; margin-bottom: 30px; }
        .header h1 { color: #facc15; font-size: 2.5em; margin-bottom: 5px; }
        .header p { color: #94a3b8; font-size: 1.1em; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 15px; }
        .card { background-color: #1e293b; padding: 15px; border-radius: 10px; border-left: 4px solid #facc15; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2); }
        .card h3 { margin: 0 0 8px 0; color: #f1f5f9; font-size: 1.1em; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .card p { margin: 4px 0; color: #cbd5e1; font-size: 0.85em; }
        .badge { background: #3b82f6; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.8em; }
        .btn { display: inline-block; width: 100%; text-align: center; margin-top: 10px; padding: 10px 0; background-color: #10b981; color: white; text-decoration: none; border-radius: 6px; font-weight: bold; transition: background 0.3s; font-size: 0.9em; }
        .btn:hover { background-color: #059669; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Singularity Ops - Striker Dashboard</h1>
            <p>Target: Top 100 High-Ticket Med Spas & Builders (Gorakhpur / Varanasi)</p>
        </div>
        <div class="grid">
"""

for index, row in df.iterrows():
    # Handle NaN values
    dm_name = str(row.get('decision_maker', 'Team')).strip()
    if dm_name == 'nan' or not dm_name:
        dm_name = 'Management'
        
    company_name = str(row['company_name']).strip()
    phone = str(row['clean_phone']).replace('+', '')
    city = str(row['city'])
    
    # Format message
    personalized_msg = raw_message.format(dm=dm_name, name=company_name)
    encoded_msg = urllib.parse.quote(personalized_msg)
    
    wa_link = f"https://api.whatsapp.com/send?phone={phone}&text={encoded_msg}"
    
    html_content += f"""
            <div class="card">
                <h3>{company_name}</h3>
                <p><strong>City:</strong> {city}</p>
                <p><strong>DM:</strong> {dm_name}</p>
                <p><span class="badge">Score: {row.get('lead_score', 'N/A')}</span></p>
                <a href="{wa_link}" target="_blank" class="btn">💬 1-Tap Pitch</a>
            </div>
    """

html_content += """
        </div>
    </div>
</body>
</html>
"""

with open("Top_100_Dashboard.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"✅ BOOM! Top_100_Dashboard.html is ready with {len(df)} High-Ticket Leads.")
