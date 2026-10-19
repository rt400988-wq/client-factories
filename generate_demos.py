import os
import urllib.parse

BASE_URL = "https://rt400988-wq.github.io/client-factories"

LEADS_DATA = [
    {"name": "Genesis Fitness Studio", "city": "Pune", "niche": "Premium Gym", "phone": "918240911029", "slug": "genesis-pune"},
    {"name": "Minimum Strength Club", "city": "Bengaluru", "niche": "Powerlifting Gym", "phone": "919324589084", "slug": "minimum-strength-blr"},
    {"name": "Meraki Fitness Studio", "city": "Kolkata", "niche": "Boutique Fitness", "phone": "917066612312", "slug": "meraki-kolkata"},
    {"name": "Viva Aesthetic Clinic", "city": "Mumbai", "niche": "Skin & Hair Clinic", "phone": "919876543210", "slug": "viva-mumbai"},
    {"name": "CosmoTree Skin Clinic", "city": "Nagpur", "niche": "Laser & Dermatology", "phone": "919123456789", "slug": "cosmotree-nagpur"},
    {"name": "Dental Hub Advanced", "city": "Pune", "niche": "Dental Clinic", "phone": "919811122334", "slug": "dentalhub-pune"},
    {"name": "Gravity Holistic Fitness", "city": "Chennai", "niche": "Holistic Studio", "phone": "919822233445", "slug": "gravity-chennai"},
    {"name": "Radhika's Balanced Body", "city": "Mumbai", "niche": "Pilates Studio", "phone": "919833344556", "slug": "radhika-pilates"},
    {"name": "Arc Clinic & Pilates", "city": "Mumbai", "niche": "Pain Science & Pilates", "phone": "919844455667", "slug": "arc-mumbai"},
    {"name": "Dr. Gauri Skin Care", "city": "Mumbai", "niche": "Dermatologist", "phone": "919855566778", "slug": "gauri-skin"},
    {"name": "Dr. Ruchi Bhirud Clinic", "city": "Pune", "niche": "Skin Specialist", "phone": "919866677889", "slug": "ruchi-pune"},
    {"name": "Oriva Skin & Hair", "city": "Rajkot", "niche": "Aesthetic Clinic", "phone": "919877788990", "slug": "oriva-rajkot"},
    {"name": "Pride Glo Aesthetics", "city": "Chennai", "niche": "Skin & Hair", "phone": "919888899001", "slug": "pride-chennai"},
    {"name": "Dermijan Skin Clinic", "city": "Chennai", "niche": "Dermatology", "phone": "919899900112", "slug": "dermijan-chennai"},
    {"name": "Twacham Skin Clinic", "city": "Indore", "niche": "Laser & Acne", "phone": "919800011223", "slug": "twacham-indore"},
    {"name": "Dr. Sakshi Dental", "city": "Udaipur", "niche": "Dental Clinic", "phone": "919811122335", "slug": "sakshi-udaipur"},
    {"name": "Infinity Dental Care", "city": "Kolkata", "niche": "Modern Dental", "phone": "919822233446", "slug": "infinity-kolkata"},
    {"name": "Chopra Dental Clinic", "city": "Delhi", "niche": "Family Dental", "phone": "919833344557", "slug": "chopra-delhi"},
    {"name": "Ivory Dental Care", "city": "Mumbai", "niche": "Sports Dental", "phone": "919844455668", "slug": "ivory-mumbai"},
    {"name": "Coach Ganesh Fitness", "city": "Jodhpur", "niche": "Strength Coach", "phone": "919855566779", "slug": "ganesh-jodhpur"},
    {"name": "FitCoach Raj", "city": "Mumbai", "niche": "Fitness Coach", "phone": "919866677890", "slug": "raj-mumbai"},
    {"name": "Vicky Mestry Rehab", "city": "Pune", "niche": "Rehab & Fitness", "phone": "919877788991", "slug": "vicky-pune"},
    {"name": "Diet with Taranjeet", "city": "Online", "niche": "Metabolic Coach", "phone": "919888899002", "slug": "taranjeet-diet"},
    {"name": "Balanced Bowls Dietitian", "city": "Pune", "niche": "Clinical Dietitian", "phone": "919899900113", "slug": "balancedbowls-pune"},
    {"name": "CA Shivani Growth", "city": "Online", "niche": "Growth Coach", "phone": "919800011224", "slug": "shivani-coach"},
    {"name": "Shabbir Padhri Career", "city": "Mumbai", "niche": "Career Coach", "phone": "919811122336", "slug": "shabbir-mumbai"},
    {"name": "Aura Fitness Hub", "city": "Hyderabad", "niche": "CrossFit Studio", "phone": "919822233447", "slug": "aura-hyd"},
    {"name": "DermaGlow Clinic", "city": "Ahmedabad", "niche": "Skin & Laser", "phone": "919833344558", "slug": "dermaglow-ahmedabad"},
    {"name": "SmileCraft Dental", "city": "Jaipur", "niche": "Orthodontics", "phone": "919844455669", "slug": "smilecraft-jaipur"},
    {"name": "Apex Fitness Lab", "city": "Surat", "niche": "Personal Training", "phone": "919855566780", "slug": "apex-surat"}
]

REQUIRED_LEAD_FIELDS = ("name", "city", "niche", "phone", "slug")
UNIQUE_LEAD_FIELDS = ("name", "phone", "slug")

def validate_leads(leads):
    """Fail fast if lead records are incomplete or share an identity field."""
    if len(leads) != 30:
        raise ValueError(f"Expected 30 leads, found {len(leads)}")
    for index, lead in enumerate(leads):
        missing = [field for field in REQUIRED_LEAD_FIELDS if not lead.get(field)]
        if missing:
            raise ValueError(f"Lead {index} is missing: {', '.join(missing)}")
    for field in UNIQUE_LEAD_FIELDS:
        values = [lead[field] for lead in leads]
        duplicates = sorted({value for value in values if values.count(value) > 1})
        if duplicates:
            raise ValueError(f"Duplicate {field} values: {duplicates}")

def build_demo_html(name, city, niche, phone, slug):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Official Booking Portal</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="bg-slate-50 text-slate-900 font-sans antialiased selection:bg-emerald-500 selection:text-white">
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-100 sticky top-0 z-50">
        <div class="max-w-3xl mx-auto px-4 py-4 flex justify-between items-center">
            <div class="flex items-center gap-2">
                <div class="w-8 h-8 rounded-lg bg-emerald-600 text-white flex items-center justify-center font-bold text-lg">⚡</div>
                <span class="font-bold text-lg text-slate-900">{name}</span>
            </div>
            <span class="text-xs bg-emerald-50 text-emerald-700 border border-emerald-200 px-3 py-1 rounded-full font-semibold">{city}</span>
        </div>
    </header>

    <main class="max-w-3xl mx-auto px-4 py-8 space-y-8">
        <div class="bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 text-white p-8 rounded-3xl shadow-2xl relative overflow-hidden">
            <div class="absolute -right-10 -bottom-10 w-48 h-48 bg-emerald-500/10 rounded-full blur-3xl"></div>
            <span class="text-xs uppercase tracking-widest text-emerald-400 font-bold mb-3 block">Premier {niche} Portal</span>
            <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight mb-4 leading-tight">Elevate Your Experience at {name}</h1>
            <p class="text-slate-300 text-base mb-8 max-w-lg">Skip the messy forms and long wait times. Book your consultation or trial session instantly via direct WhatsApp concierge.</p>
            <a href="https://wa.me/{phone}?text=Hi%20{name}%20Team,%20I%20checked%20your%20digital%20booking%20portal%20and%20would%20like%20to%20schedule%20an%20appointment." target="_blank" class="bg-emerald-500 hover:bg-emerald-600 text-white font-bold py-4 px-8 rounded-2xl flex items-center justify-center gap-3 shadow-lg shadow-emerald-500/30 transition transform hover:-translate-y-0.5">
                <i data-lucide="message-circle" class="w-6 h-6"></i> Book on WhatsApp Now
            </a>
        </div>

        <div class="bg-white p-6 sm:p-8 rounded-3xl border border-slate-100 shadow-xl space-y-6">
            <h2 class="text-xl font-bold text-slate-900">Instant Inquiry Assistant</h2>
            <p class="text-sm text-slate-500">Select your requirement below to auto-generate your booking message:</p>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <button onclick="setIntent('Consultation / General Inquiry')" class="intent-btn p-4 rounded-xl border border-slate-200 text-left font-medium text-sm hover:border-emerald-500 hover:bg-emerald-50/50 transition">
                    💬 General Consultation
                </button>
                <button onclick="setIntent('First-Time Trial / Special Session')" class="intent-btn p-4 rounded-xl border border-slate-200 text-left font-medium text-sm hover:border-emerald-500 hover:bg-emerald-50/50 transition">
                    ⭐ First-Time Trial Pass
                </button>
            </div>

            <div class="pt-4 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
                <span id="selected-intent" class="text-xs text-slate-500 italic">Selected: General Consultation</span>
                <a id="wa-final-btn" href="https://wa.me/{phone}?text=Hi%20{name},%20I%20would%20like%20to%20book%20a%20Consultation%20/%20General%20Inquiry." target="_blank" class="w-full sm:w-auto bg-slate-900 hover:bg-slate-800 text-white font-semibold py-3 px-6 rounded-xl text-center text-sm transition">
                    Send to WhatsApp →
                </a>
            </div>
        </div>
    </main>

    <footer class="text-center py-8 text-xs text-slate-400 border-t border-slate-100 mt-12">
        Powered by AI High-Conversion Funnels &bull; {name} &copy; 2026
    </footer>

    <script>
        lucide.createIcons();
        let currentChoice = "Consultation / General Inquiry";
        function setIntent(intent) {{
            currentChoice = intent;
            document.getElementById('selected-intent').innerText = "Selected: " + intent;
            const encoded = encodeURIComponent("Hi {name}, I would like to book a " + intent + ".");
            document.getElementById('wa-final-btn').href = "https://wa.me/{phone}?text=" + encoded;
        }}
    </script>
</body>
</html>
"""

def build_dashboard_html(leads):
    cards_html = ""
    for lead in leads:
        demo_url = f"{BASE_URL}/demos/{lead['slug']}/"
        pitch = f"Hi {lead['name']} Team! Main {lead['city']} ke local businesses ke liye high-converting WhatsApp booking funnels banata hu. Aapke brand ke liye maine ek custom Live Demo ready kiya hai: {demo_url} . Ek baar open karke dekhiye—ispe clients bina form bhare seedha aapke WhatsApp par appointment book kar sakte hain. Pasand aaye toh batayiyega!"
        encoded_pitch = urllib.parse.quote(pitch)
        wa_link = f"https://wa.me/{lead['phone']}?text={encoded_pitch}"
        demo_link = f"demos/{lead['slug']}/index.html"

        cards_html += f"""
        <div class="bg-white p-6 rounded-3xl border border-slate-100 shadow-xl space-y-4 flex flex-col justify-between">
            <div>
                <div class="flex justify-between items-start mb-2">
                    <span class="text-xs bg-indigo-50 text-indigo-700 font-semibold px-3 py-1 rounded-full">{lead['niche']}</span>
                    <span class="text-xs bg-slate-100 text-slate-600 font-medium px-2.5 py-1 rounded-md">{lead['city']}</span>
                </div>
                <h3 class="text-lg font-bold text-slate-900">{lead['name']}</h3>
                <p class="text-xs text-slate-400 font-mono mt-1">WhatsApp: +{lead['phone']}</p>
            </div>
            
            <div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-100">
                <a href="{demo_link}" target="_blank" class="bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold py-3 px-4 rounded-xl text-center transition flex items-center justify-center gap-1.5">
                    👁️ Preview Demo
                </a>
                <a href="{wa_link}" target="_blank" class="bg-emerald-500 hover:bg-emerald-600 text-white text-xs font-bold py-3 px-4 rounded-xl text-center transition flex items-center justify-center gap-1.5 shadow-lg shadow-emerald-500/20">
                    💬 1-Tap Pitch
                </a>
            </div>
        </div>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Client Striker Dashboard | Zero-Cost Agency</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="bg-slate-100 text-slate-900 font-sans antialiased">
    <header class="bg-slate-900 text-white border-b border-slate-800 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
            <div class="flex items-center gap-2">
                <span class="text-xl">🚀</span>
                <h1 class="text-lg font-bold tracking-tight">Client Striker Dashboard</h1>
            </div>
            <span class="text-xs bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 px-3 py-1 rounded-full font-semibold">30 Active Sniper Leads</span>
        </div>
    </header>

    <main class="max-w-6xl mx-auto px-4 py-8 space-y-8">
        <div class="bg-gradient-to-r from-emerald-600 to-teal-700 text-white p-6 sm:p-8 rounded-3xl shadow-xl flex flex-col sm:flex-row justify-between items-center gap-6">
            <div>
                <h2 class="text-2xl font-bold mb-2">14-Day ₹28,000+ Execution Hub</h2>
                <p class="text-emerald-100 text-sm max-w-xl">Tap <strong class="underline">1-Tap Pitch</strong> below. WhatsApp opens automatically with your pre-built custom demo link and customized Hinglish pitch. Send 10 per day!</p>
            </div>
            <div class="bg-white/10 backdrop-blur-md px-6 py-4 rounded-2xl border border-white/20 text-center">
                <span class="block text-2xl font-extrabold">30</span>
                <span class="text-xs uppercase tracking-wider text-emerald-200 font-medium">Ready Demos</span>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {cards_html}
        </div>
    </main>

    <footer class="text-center py-12 text-xs text-slate-500">
        Zero-Cost Agency Automation &bull; Built for Maximum Speed ⚡
    </footer>
</body>
</html>
"""

def main():
    validate_leads(LEADS_DATA)
    os.makedirs("demos", exist_ok=True)
    for lead in LEADS_DATA:
        folder = os.path.join("demos", lead["slug"])
        os.makedirs(folder, exist_ok=True)
        html_content = build_demo_html(
            lead["name"], lead["city"], lead["niche"], lead["phone"], lead["slug"]
        )
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)

    dashboard_content = build_dashboard_html(LEADS_DATA)
    with open("dashboard.html", "w", encoding="utf-8") as f:
        f.write(dashboard_content)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(dashboard_content)

    print("Generated successfully!")

if __name__ == "__main__":
    main()
