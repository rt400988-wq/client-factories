import os
import urllib.parse

BASE_URL = "https://rt400988-wq.github.io/client-factories"

# 45 100% REAL VERIFIED LEADS (Batch A: Linktree Verified, Batch B: Google Maps No-Website, Batch C: Google Maps Static Website)
LEADS_DATA = [
    # --- BATCH A: 15 LINKTREE VERIFIED DOCTORS, CLINICS & STUDIOS (HIGHEST PRIORITY) ---
    {"id": 1, "name": "Health India Gym", "city": "India", "niche": "Gym & Fitness", "template": "fitness", "category": "linktree", "phone": "919313681999", "ig": "https://www.instagram.com/healthindiagym99", "proof": "linktr.ee/healthindiagym", "slug": "health-india-gym"},
    {"id": 2, "name": "Jaya Physio Clinics", "city": "Hyderabad", "niche": "Physiotherapy & Sports Rehab", "template": "medical", "category": "linktree", "phone": "919849695691", "ig": "https://www.instagram.com/jayaphysioclinics", "proof": "linktr.ee/jayaphysioclinics", "slug": "jaya-physio-hyd"},
    {"id": 3, "name": "Dr. Aditya Raj Spine Clinic", "city": "Mumbai (Bandra & Andheri)", "niche": "Orthopedic Spine Surgeon", "template": "medical", "category": "linktree", "phone": "919372671858", "ig": "https://www.instagram.com/draditya_raj/", "proof": "linktr.ee/draditya_raj", "slug": "dr-aditya-raj-mumbai"},
    {"id": 4, "name": "Dr. Supreet Bajwa Ortho", "city": "Mumbai", "niche": "Knee & Hip Replacement Surgeon", "template": "medical", "category": "linktree", "phone": "919820727046", "ig": "https://www.instagram.com/drbajwaortho", "proof": "linktr.ee/drsupreetbajwa", "slug": "dr-supreet-bajwa"},
    {"id": 5, "name": "Dr. Nimish Kulkarni Clinic", "city": "Mumbai (Bandra West)", "niche": "Paediatrician & Child Nutrition", "template": "medical", "category": "linktree", "phone": "917506074017", "ig": "https://www.instagram.com/drnimishkulkarni", "proof": "linktr.ee/drnimishk", "slug": "dr-nimish-kulkarni"},
    {"id": 6, "name": "Bangalore Pain Clinic", "city": "Bangalore", "niche": "Non-Surgical Pain Management", "template": "medical", "category": "linktree", "phone": "918282827623", "ig": "https://www.instagram.com/bangalorepainclinics", "proof": "linktr.ee/Bangalorepc", "slug": "bangalore-pain-clinic"},
    {"id": 7, "name": "Solace Life Clinic", "city": "Bengaluru", "niche": "Diabetes & Metabolic Care", "template": "medical", "category": "linktree", "phone": "918550045678", "ig": "https://www.instagram.com/solacelifeclinic", "proof": "linktr.ee/solacelife", "slug": "solace-life-blr"},
    {"id": 8, "name": "CURADOR Physio & Sports Rehab", "city": "Pune", "niche": "Physiotherapy & Rehab Centre", "template": "medical", "category": "linktree", "phone": "919689912426", "ig": "https://www.instagram.com/curadorphysio/", "proof": "linktr.ee/curadorphysio", "slug": "curador-physio-pune"},
    {"id": 9, "name": "Alleviate Pain Clinic", "city": "Bangalore", "niche": "Pain Management Specialist", "template": "medical", "category": "linktree", "phone": "919606695761", "ig": "https://www.instagram.com/alleviatepainclinic", "proof": "linktr.ee/dhruvi0616", "slug": "alleviate-pain-blr"},
    {"id": 10, "name": "Beautiful Mind Healthcare", "city": "Bangalore", "niche": "Mental Health & Wellness", "template": "medical", "category": "linktree", "phone": "917760420485", "ig": "https://www.instagram.com/beautifulmindhealthcare", "proof": "linktr.ee/beautifulmindhealthcare", "slug": "beautiful-mind-blr"},
    {"id": 11, "name": "Revive Motion Physiotherapy", "city": "New Delhi", "niche": "Physiotherapy & Recovery", "template": "medical", "category": "linktree", "phone": "918447547440", "ig": "https://www.instagram.com/physiotherapyclinics/", "proof": "linktr.ee/revivemotion", "slug": "revive-motion-delhi"},
    {"id": 12, "name": "Dr. Santosh Kumar Ortho", "city": "Kolkata", "niche": "Orthopaedic Surgeon", "template": "medical", "category": "linktree", "phone": "919831911584", "ig": "https://www.instagram.com/drsantoshkumarortho", "proof": "linktr.ee/drsantoshkumar", "slug": "dr-santosh-kolkata"},
    {"id": 13, "name": "Luxury Aesthetics Clinic", "city": "New Delhi", "niche": "Skin, Hair & Body Clinic", "template": "aesthetics", "category": "linktree", "phone": "917290015801", "ig": "https://www.instagram.com/luxuryaesthetics_clinic", "proof": "linktr.ee/LAclinic", "slug": "luxury-aesthetics-delhi"},
    {"id": 14, "name": "Gravity Holistic Fitness", "city": "Chennai", "niche": "Holistic Fitness & Physio", "template": "fitness", "category": "linktree", "phone": "917550110863", "ig": "https://www.instagram.com/gravityholisticfitness", "proof": "linktr.ee/GravityHolisticFitness", "slug": "gravity-holistic-chennai"},
    {"id": 15, "name": "Dr. Hans Centre for ENT", "city": "Delhi NCR & Gurugram", "niche": "ENT Specialist Care", "template": "medical", "category": "linktree", "phone": "919811703926", "ig": "https://www.instagram.com/drhans.ent/", "proof": "linktr.ee/drjmhans", "slug": "dr-hans-ent-delhi"},

    # --- BATCH B: 15 GOOGLE MAPS "NO-WEBSITE" CLINICS & GYMS (FASTEST CLOSERS) ---
    {"id": 16, "name": "The Nice Skin Clinic", "city": "Pune (Koregaon Park)", "niche": "Skin & Laser Clinic", "template": "aesthetics", "category": "no_website", "phone": "918007587255", "ig": "https://www.google.com/search?q=The+Nice+Skin+Clinic+Pune+Instagram", "proof": "4.8★ (352 Google Reviews)", "slug": "nice-skin-pune"},
    {"id": 17, "name": "Dr. Sachin Kashid Skin Clinic", "city": "Pune (Hadapsar)", "niche": "Dermatologist & Laser Specialist", "template": "aesthetics", "category": "no_website", "phone": "919028472129", "ig": "https://www.google.com/search?q=Dr+Sachin+Kashid+Pune+Instagram", "proof": "4.6★ (421 Google Reviews)", "slug": "dr-sachin-kashid-pune"},
    {"id": 18, "name": "SLV Dental & Implant Center", "city": "Bangalore (HSR Layout)", "niche": "Dental & Implant Clinic", "template": "medical", "category": "no_website", "phone": "918095384902", "ig": "https://www.google.com/search?q=SLV+Dental+Clinic+HSR+Bangalore", "proof": "5.0★ (1,029 Google Reviews)", "slug": "slv-dental-blr"},
    {"id": 19, "name": "Smile Dental Clinic", "city": "Bangalore (Koramangala)", "niche": "Advanced Dental Care", "template": "medical", "category": "no_website", "phone": "919845192325", "ig": "https://www.google.com/search?q=Smile+Dental+Clinic+Koramangala", "proof": "4.9★ (407 Google Reviews)", "slug": "smile-dental-blr"},
    {"id": 20, "name": "Dr. Muchhala Dental Clinic", "city": "Mumbai (Borivali West)", "niche": "Dental & Cosmetic Clinic", "template": "medical", "category": "no_website", "phone": "919137824428", "ig": "https://www.google.com/search?q=Dr+Muchhala+Dental+Clinic+Borivali", "proof": "4.9★ (260 Google Reviews)", "slug": "dr-muchhala-dental"},
    {"id": 21, "name": "Creed Culture Gym", "city": "Mumbai (Kandivali West)", "niche": "Strength & Conditioning Gym", "template": "fitness", "category": "no_website", "phone": "919372161805", "ig": "https://www.instagram.com/creedculturegym", "proof": "4.3★ (431 Google Reviews)", "slug": "creed-culture-mumbai"},
    {"id": 22, "name": "FM Studio Gym", "city": "Mumbai (Powai)", "niche": "Premium Fitness Studio", "template": "fitness", "category": "no_website", "phone": "919137603351", "ig": "https://www.google.com/search?q=FM+Studio+Gym+Powai+Instagram", "proof": "4.9★ (276 Google Reviews)", "slug": "fm-studio-powai"},
    {"id": 23, "name": "Pilates Academy Bandra", "city": "Mumbai (Bandra West)", "niche": "Boutique Pilates Studio", "template": "fitness", "category": "no_website", "phone": "919819766765", "ig": "https://www.google.com/search?q=Pilates+Academy+Bandra+Instagram", "proof": "4.9★ (120 Google Reviews)", "slug": "pilates-academy-bandra"},
    {"id": 24, "name": "The Pilates Story", "city": "Mumbai (Borivali West)", "niche": "Pilates & Movement Studio", "template": "fitness", "category": "no_website", "phone": "919167333100", "ig": "https://www.google.com/search?q=The+Pilates+Story+Borivali+Instagram", "proof": "5.0★ (70 Google Reviews)", "slug": "pilates-story-mumbai"},
    {"id": 25, "name": "Pilates Academy Worli", "city": "Mumbai (Worli)", "niche": "Luxury Pilates Studio", "template": "fitness", "category": "no_website", "phone": "919967876765", "ig": "https://www.google.com/search?q=Pilates+Academy+Worli+Instagram", "proof": "4.9★ (64 Google Reviews)", "slug": "pilates-academy-worli"},
    {"id": 26, "name": "My Pilates Studio", "city": "Mumbai (Santacruz West)", "niche": "Core & Pilates Studio", "template": "fitness", "category": "no_website", "phone": "919892383095", "ig": "https://www.google.com/search?q=My+Pilates+Studio+Santacruz+Instagram", "proof": "4.7★ (64 Google Reviews)", "slug": "my-pilates-santacruz"},
    {"id": 27, "name": "Transform Wellness Studio", "city": "Pune (Kalyani Nagar)", "niche": "Personal & Group Training", "template": "fitness", "category": "no_website", "phone": "919890350005", "ig": "https://www.google.com/search?q=Transform+Wellness+Kalyani+Nagar+Pune", "proof": "4.8★ (224 Google Reviews)", "slug": "transform-wellness-pune"},
    {"id": 28, "name": "Ethcure Fitness Club", "city": "Pune (Kothrud)", "niche": "Fitness & Transformation Club", "template": "fitness", "category": "no_website", "phone": "917887955559", "ig": "https://www.google.com/search?q=Ethcure+Fitness+Club+Kothrud+Instagram", "proof": "4.9★ (158 Google Reviews)", "slug": "ethcure-fitness-pune"},
    {"id": 29, "name": "La Fit Gym Kothrud", "city": "Pune (Kothrud)", "niche": "Strength & Fitness Gym", "template": "fitness", "category": "no_website", "phone": "918408804848", "ig": "https://www.google.com/search?q=La+Fit+Gym+Kothrud+Pune+Instagram", "proof": "4.9★ (51 Google Reviews)", "slug": "la-fit-pune"},
    {"id": 30, "name": "Prime Fitness Club", "city": "Bangalore (Marathahalli)", "niche": "Mega Fitness & Strength Club", "template": "fitness", "category": "no_website", "phone": "917411784815", "ig": "https://www.google.com/search?q=Prime+Fitness+Club+Marathahalli+Instagram", "proof": "4.5★ (331 Google Reviews)", "slug": "prime-fitness-blr"},

    # --- BATCH C: 15 HIGH-TICKET CLINICS & STUDIOS (UPGRADE TO AI WHATSAPP FUNNEL) ---
    {"id": 31, "name": "The Clinic by Dr. Zara", "city": "Mumbai (Juhu)", "niche": "Luxury Skin & Laser Clinic", "template": "aesthetics", "category": "upgrade", "phone": "918591741112", "ig": "https://drzaratheclinic.com", "proof": "5.0★ (1,091 Reviews) | drzaratheclinic.com", "slug": "dr-zara-juhu"},
    {"id": 32, "name": "Everything Skin & Hair - Dr. Punit", "city": "Mumbai (Juhu)", "niche": "Clinical Dermatology & Hair", "template": "aesthetics", "category": "upgrade", "phone": "919833003229", "ig": "https://everythingskinhair.com", "proof": "4.9★ (1,549 Reviews) | everythingskinhair.com", "slug": "dr-punit-saraogi"},
    {"id": 33, "name": "Carewell Clinic - Dr. Manjrekar", "city": "Mumbai (Andheri East)", "niche": "Skin, Laser & Hair Clinic", "template": "aesthetics", "category": "upgrade", "phone": "918291932733", "ig": "https://ccarewellskinlaserhairclinic.com", "proof": "4.9★ (699 Reviews) | Andheri East", "slug": "carewell-clinic-mumbai"},
    {"id": 34, "name": "Cutis Skin Clinic", "city": "Mumbai (Andheri West)", "niche": "Skin & Aesthetic Clinic", "template": "aesthetics", "category": "upgrade", "phone": "919833889680", "ig": "https://cutis.in", "proof": "4.8★ (1,510 Reviews) | cutis.in", "slug": "cutis-skin-mumbai"},
    {"id": 35, "name": "Sweat Pilates Studio", "city": "Mumbai (Andheri West)", "niche": "Premier Pilates & Wellness", "template": "fitness", "category": "upgrade", "phone": "919920116603", "ig": "https://sweatfitwellness.com", "proof": "4.9★ (1,359 Reviews) | sweatfitwellness.com", "slug": "sweat-pilates-mumbai"},
    {"id": 36, "name": "Sheetal Core Pilates", "city": "Mumbai (Worli)", "niche": "Core Pilates Studio", "template": "fitness", "category": "upgrade", "phone": "919820503409", "ig": "https://corepilates.in", "proof": "4.9★ (81 Reviews) | corepilates.in", "slug": "sheetal-core-pilates"},
    {"id": 37, "name": "PPS Pure Pilates Studio", "city": "Mumbai (Kandivali West)", "niche": "Pilates & Posture Studio", "template": "fitness", "category": "upgrade", "phone": "919167252996", "ig": "https://purepilates.co.in", "proof": "4.9★ (44 Reviews) | purepilates.co.in", "slug": "pure-pilates-mumbai"},
    {"id": 38, "name": "The Space Fitness", "city": "Mumbai (Juhu)", "niche": "Boutique Fitness Studio", "template": "fitness", "category": "upgrade", "phone": "919619348427", "ig": "https://thespacefitness.in", "proof": "4.7★ (124 Reviews) | thespacefitness.in", "slug": "the-space-juhu"},
    {"id": 39, "name": "Taj Skin Hair Laser Clinic", "city": "Pune (Kothrud)", "niche": "Dermatologist & Laser Center", "template": "aesthetics", "category": "upgrade", "phone": "917796969797", "ig": "https://tajskin.in", "proof": "4.9★ (775 Reviews) | tajskin.in", "slug": "taj-skin-pune"},
    {"id": 40, "name": "Dermaplus Skin Clinic", "city": "Pune (Aundh)", "niche": "Advanced Dermatology Clinic", "template": "aesthetics", "category": "upgrade", "phone": "917009219058", "ig": "https://dermaplusclinic.in", "proof": "4.8★ (1,615 Reviews) | dermaplusclinic.in", "slug": "dermaplus-pune"},
    {"id": 41, "name": "Derma Touch Skin Laser Clinic", "city": "Pune (Kharadi)", "niche": "Skin, Laser & Hair Clinic", "template": "aesthetics", "category": "upgrade", "phone": "918055398727", "ig": "https://dermatouchindia.com", "proof": "4.8★ (1,461 Reviews) | dermatouchindia.com", "slug": "derma-touch-pune"},
    {"id": 42, "name": "Leor Skin, Hair & Body Clinic", "city": "Pune (Koregaon Park)", "niche": "Luxury Aesthetic Clinic", "template": "aesthetics", "category": "upgrade", "phone": "919890691515", "ig": "https://leorclinics.com", "proof": "4.8★ (1,078 Reviews) | leorclinics.com", "slug": "leor-clinic-pune"},
    {"id": 43, "name": "Moushu Pilates Studio", "city": "Pune (Kalyani Nagar)", "niche": "Pilates Studio & Education", "template": "fitness", "category": "upgrade", "phone": "919028306301", "ig": "https://moushuspilates.com", "proof": "5.0★ (70 Reviews) | moushuspilates.com", "slug": "moushu-pilates-pune"},
    {"id": 44, "name": "K6 Fitness Studios", "city": "Pune (Kalyani Nagar)", "niche": "Premium Fitness Studio", "template": "fitness", "category": "upgrade", "phone": "919579139729", "ig": "https://k6fitnessstudios.in", "proof": "4.9★ (233 Reviews) | k6fitnessstudios.in", "slug": "k6-fitness-pune"},
    {"id": 45, "name": "WILDFIT Personal Training", "city": "Pune (Kalyani Nagar)", "niche": "Nutrition & Personal Training", "template": "fitness", "category": "upgrade", "phone": "919903033004", "ig": "https://wildfit.me", "proof": "4.9★ (204 Reviews) | wildfit.me", "slug": "wildfit-pune"}
]


def validate_dataset(leads):
    phones = [item["phone"] for item in leads]
    slugs = [item["slug"] for item in leads]
    assert len(phones) == len(set(phones)), "CRITICAL ERROR: Duplicate phone number detected!"
    assert len(slugs) == len(set(slugs)), "CRITICAL ERROR: Duplicate slug detected!"
    for item in leads:
        assert len(item["phone"]) == 12 and item["phone"].startswith("91"), f"Invalid phone format for {item['name']}: {item['phone']}"
    print(f"✅ STRICT VALIDATION PASSED: All {len(leads)} leads have 100% unique phones & slugs!")


def get_niche_options(template_type):
    if template_type == "aesthetics":
        return [
            "✨ Acne, Scars & Pigmentation Treatment",
            "💎 Laser Hair Reduction / Medi-Facial",
            "🌿 Hair Fall, PRP & Scalp Consultation",
            "🌟 Anti-Aging & Skin Glow Assessment"
        ], "amber-500", "from-stone-900 via-neutral-900 to-stone-950", " Take 30-Sec Skin & Hair Assessment"
    elif template_type == "medical":
        return [
            "🩺 Specialist Doctor Consultation",
            "🦴 Pain Relief / Rehab / Procedure Inquiry",
            "🦷 Complete Checkup & Diagnostic Scan",
            "⚡ Priority Same-Day Appointment Slot"
        ], "teal-500", "from-slate-900 via-teal-950 to-slate-900", "Book Priority Patient Consultation"
    else:
        return [
            "🔥 Claim 1-Day VIP Trial Session",
            "💪 Personal Training & Body Transformation",
            "🧘‍♀️ Pilates / Core / Mobility Batch Inquiry",
            "🥗 Custom Nutrition & Membership Plans"
        ], "emerald-500", "from-zinc-900 via-emerald-950 to-zinc-950", "Claim Free Trial & Fitness Assessment"


def build_demo_html(lead):
    name = lead["name"]
    city = lead["city"]
    niche = lead["niche"]
    phone = lead["phone"]
    proof = lead["proof"]
    options, accent, bg_grad, quiz_title = get_niche_options(lead["template"])

    first_opt_encoded = urllib.parse.quote(f"Hi {name} Team! I visited your official booking portal and want to inquire about: {options[0]}")
    hero_wa_encoded = urllib.parse.quote(f"Hi {name} Team! I visited your booking portal and would like to book an appointment.")

    buttons_html = ""
    for opt in options:
        safe_opt = opt.replace("'", "\\'")
        buttons_html += f"""
        <button onclick="selectOption('{safe_opt}', this)" class="opt-btn p-4 rounded-2xl border-2 border-slate-200 text-left font-semibold text-sm hover:border-slate-900 transition flex items-center justify-between group">
            <span>{opt}</span>
            <span class="text-slate-400 group-hover:text-slate-900">→</span>
        </button>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} — {city} | Official Booking Portal</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="bg-slate-50 text-slate-900 font-sans antialiased">
    <header class="bg-white/90 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-3xl mx-auto px-4 py-3.5 flex justify-between items-center">
            <div>
                <h1 class="font-extrabold text-base sm:text-lg text-slate-900 leading-tight">{name}</h1>
                <p class="text-xs text-slate-500">{niche} • {city}</p>
            </div>
            <span class="text-xs bg-emerald-50 text-emerald-700 border border-emerald-200 px-3 py-1 rounded-full font-bold">Verified Portal</span>
        </div>
    </header>

    <main class="max-w-3xl mx-auto px-4 py-6 sm:py-10 space-y-8">
        <!-- Hero Card -->
        <div class="bg-gradient-to-br {bg_grad} text-white p-7 sm:p-10 rounded-3xl shadow-2xl relative overflow-hidden">
            <div class="inline-flex items-center gap-2 bg-white/10 border border-white/15 px-3 py-1 rounded-full text-xs font-semibold mb-4">
                <span>⭐ {proof}</span>
            </div>
            <h2 class="text-2xl sm:text-4xl font-extrabold tracking-tight mb-3 leading-tight">{name}</h2>
            <p class="text-slate-300 text-sm sm:text-base mb-7 max-w-xl">Skip long waiting calls and forms. Select your requirement below and connect directly with our {city} concierge desk on WhatsApp in 10 seconds.</p>
            <a href="https://wa.me/{phone}?text={hero_wa_encoded}" target="_blank" class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-extrabold py-4 px-7 rounded-2xl inline-flex items-center justify-center gap-2.5 shadow-lg transition w-full sm:w-auto">
                💬 Instant WhatsApp Booking
            </a>
        </div>

        <!-- 30-Sec Interactive Funnel -->
        <div class="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-xl space-y-6">
            <div>
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-600">Step 1 of 2 • Fast Intake</span>
                <h3 class="text-xl font-extrabold text-slate-900 mt-1">{quiz_title}</h3>
                <p class="text-xs sm:text-sm text-slate-500 mt-1">Tap your primary goal below to pre-fill your priority WhatsApp consultation pass:</p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {buttons_html}
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                <input id="patient-name" type="text" placeholder="Your Name (Optional)" oninput="updateLink()" class="w-full px-4 py-3 rounded-xl border border-slate-200 text-sm focus:outline-none focus:border-slate-900">
                <select id="slot-time" onchange="updateLink()" class="w-full px-4 py-3 rounded-xl border border-slate-200 text-sm bg-white focus:outline-none focus:border-slate-900">
                    <option value="Morning Slot (10 AM - 1 PM)">Preferred: Morning (10 AM - 1 PM)</option>
                    <option value="Afternoon Slot (1 PM - 5 PM)">Preferred: Afternoon (1 PM - 5 PM)</option>
                    <option value="Evening Slot (5 PM - 8 PM)">Preferred: Evening (5 PM - 8 PM)</option>
                </select>
            </div>

            <div class="pt-4 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
                <span id="chosen-label" class="text-xs font-semibold text-slate-600">Selected: {options[0]}</span>
                <a id="wa-submit-btn" href="https://wa.me/{phone}?text={first_opt_encoded}" target="_blank" class="w-full sm:w-auto bg-slate-900 hover:bg-slate-800 text-white font-bold py-4 px-8 rounded-2xl text-center text-sm transition shadow-lg">
                    Send Priority Request on WhatsApp →
                </a>
            </div>
        </div>
    </main>

    <footer class="text-center py-8 text-xs text-slate-400">
        {name} ({city}) • Direct WhatsApp Concierge (+{phone})
    </footer>

    <script>
        const BUSINESS_NAME = {repr(name)};
        const PHONE = "{phone}";
        let selectedGoal = {repr(options[0])};

        function selectOption(goal, btn) {{
            selectedGoal = goal;
            document.querySelectorAll('.opt-btn').forEach(b => {{
                b.classList.remove('border-slate-900', 'bg-slate-50');
                b.classList.add('border-slate-200');
            }});
            btn.classList.remove('border-slate-200');
            btn.classList.add('border-slate-900', 'bg-slate-50');
            document.getElementById('chosen-label').innerText = "Selected: " + goal;
            updateLink();
        }}

        function updateLink() {{
            const userName = document.getElementById('patient-name').value.trim();
            const slot = document.getElementById('slot-time').value;
            const namePart = userName ? "My name is " + userName + ". " : "";
            const msg = "Hi " + BUSINESS_NAME + " Team! " + namePart + "I want to book: " + selectedGoal + " (" + slot + ").";
            document.getElementById('wa-submit-btn').href = "https://wa.me/" + PHONE + "?text=" + encodeURIComponent(msg);
        }}
    </script>
</body>
</html>
"""


def build_custom_pitch(lead, demo_url):
    name = lead["name"]
    city = lead["city"]
    cat = lead["category"]
    proof = lead["proof"]

    if cat == "linktree":
        return (
            f"Hi {name} Team! 👋 Main abhi aapka Instagram aur Linktree ({proof}) dekh raha tha. "
            f"Aapka profile kaafi strong hai, par basic Linktree me multiple links hone se kaafi patients/clients bina book kiye drop ho jaate hain.\n\n"
            f"Isliye maine aapke naam se ek custom *1-Click Interactive Assessment & WhatsApp Booking Portal* ready kiya hai:\n"
            f"👉 {demo_url}\n\n"
            f"Ek baar phone par open karke dekhiye—isme client apni requirement select karke 10 seconds me seedha aapke isi WhatsApp number par pre-filled message ke sath land karega. Kaisa laga aapko yeh upgrade?"
        )
    elif cat == "no_website":
        return (
            f"Hi {name} Team! 👋 Maine Google Maps par dekha ki {city} me aapke {proof} hain, "
            f"lekin Maps aur Instagram par aapka koi official Direct Booking Portal nahi tha (jis wajah se kaafi inquiries Practo/Justdial par dusre competitors ko chali jaati hain).\n\n"
            f"Maine aapke brand ke liye ek custom *Official Instant WhatsApp Booking Portal* ka live demo banaya hai:\n"
            f"👉 {demo_url}\n\n"
            f"Isko aap aaj hi apne Google Maps ke 'Website' button aur Instagram Bio me laga sakte hain. Ek baar khol kar check kijiye aur batayiye kaisa laga!"
        )
    else:
        return (
            f"Hi {name} Team! 👋 Aapke {city} center ke Google reviews ({proof}) kaafi impressive hain! "
            f"Instagram aur Google se aane wale mobile visitors ke liye maine ek *Fast 30-Second Interactive WhatsApp Lead Funnel* ready kiya hai (jo normal website form ke muqable 3x zyada inquiries convert karta hai):\n"
            f"👉 {demo_url}\n\n"
            f"Ek baar open karke 'Step 1 Assessment' try kijiye—yeh visitor ki exact requirement puch kar seedha aapke WhatsApp par pre-filled booking le aata hai. Pasand aaye toh batayiyega!"
        )


def build_dashboard_html(leads):
    cards_html = ""
    for lead in leads:
        demo_url = f"{BASE_URL}/demos/{lead['slug']}/"
        pitch_text = build_custom_pitch(lead, demo_url)
        encoded_pitch = urllib.parse.quote(pitch_text)
        wa_link = f"https://wa.me/{lead['phone']}?text={encoded_pitch}"
        local_preview = f"demos/{lead['slug']}/index.html"

        badge_color = (
            "bg-amber-100 text-amber-800 border-amber-300" if lead["category"] == "linktree"
            else "bg-emerald-100 text-emerald-800 border-emerald-300" if lead["category"] == "no_website"
            else "bg-indigo-100 text-indigo-800 border-indigo-300"
        )
        badge_label = (
            "🔥 Priority 1: Replace Linktree" if lead["category"] == "linktree"
            else "⚡ Priority 1: No Website on Maps" if lead["category"] == "no_website"
            else "💎 Priority 2: Funnel Upgrade"
        )

        cards_html += f"""
        <div class="lead-card bg-white p-6 rounded-3xl border border-slate-200 shadow-sm hover:shadow-xl transition flex flex-col justify-between space-y-5" data-category="{lead['category']}">
            <div class="space-y-2.5">
                <div class="flex justify-between items-center gap-2">
                    <span class="text-[11px] font-extrabold px-2.5 py-1 rounded-full border {badge_color}">{badge_label}</span>
                    <span class="text-xs font-bold text-slate-400">#{lead['id']}</span>
                </div>
                <h3 class="text-lg font-extrabold text-slate-900 leading-snug">{lead['name']}</h3>
                <p class="text-xs font-semibold text-slate-600">{lead['niche']} • <span class="text-slate-900">{lead['city']}</span></p>
                <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-100 text-[11px] text-slate-500 font-mono space-y-1">
                    <div>📞 WA: +{lead['phone']}</div>
                    <div class="truncate">✅ Proof: {lead['proof']}</div>
                </div>
            </div>

            <div class="space-y-2 pt-2 border-t border-slate-100">
                <div class="grid grid-cols-2 gap-2">
                    <a href="{local_preview}" target="_blank" class="bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold py-2.5 px-3 rounded-xl text-center transition">
                        👁️ Preview Demo
                    </a>
                    <a href="{lead['ig']}" target="_blank" class="bg-pink-50 hover:bg-pink-100 text-pink-700 border border-pink-200 text-xs font-bold py-2.5 px-3 rounded-xl text-center transition">
                        📸 IG / Source
                    </a>
                </div>
                <a href="{wa_link}" target="_blank" class="w-full bg-emerald-500 hover:bg-emerald-600 text-white text-xs font-extrabold py-3.5 px-4 rounded-xl text-center transition flex items-center justify-center gap-2 shadow-md shadow-emerald-500/20">
                    💬 1-Tap WhatsApp Pitch ({lead['name'][:18]}...)
                </a>
            </div>
        </div>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>45 Verified Leads Striker Hub | 13-Day ₹28k Sprint</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-100 text-slate-900 font-sans antialiased">
    <header class="bg-slate-950 text-white sticky top-0 z-50 border-b border-slate-800">
        <div class="max-w-6xl mx-auto px-4 py-4 flex flex-wrap justify-between items-center gap-3">
            <div class="flex items-center gap-2.5">
                <span class="text-xl">🔫👽</span>
                <div>
                    <h1 class="text-base sm:text-lg font-extrabold tracking-tight">Singularity Striker Hub v2.0</h1>
                    <p class="text-[11px] text-slate-400">45 100% Real Verified Leads • Zero Duplicate Numbers • 1-to-1 Locked Links</p>
                </div>
            </div>
            <div class="flex gap-2">
                <button onclick="filterCards('all')" class=" text-xs bg-slate-800 hover:bg-slate-700 px-3 py-1.5 rounded-lg font-bold">All (45)</button>
                <button onclick="filterCards('linktree')" class="text-xs bg-amber-500/20 text-amber-300 border border-amber-500/30 px-3 py-1.5 rounded-lg font-bold">Linktree (15)</button>
                <button onclick="filterCards('no_website')" class="text-xs bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 px-3 py-1.5 rounded-lg font-bold">No-Website (15)</button>
                <button onclick="filterCards('upgrade')" class="text-xs bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 px-3 py-1.5 rounded-lg font-bold">Upgrades (15)</button>
            </div>
        </div>
    </header>

    <main class="max-w-6xl mx-auto px-4 py-8 space-y-6">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {cards_html}
        </div>
    </main>

    <script>
        function filterCards(cat) {{
            document.querySelectorAll('.lead-card').forEach(card => {{
                if (cat === 'all' || card.dataset.category === cat) {{
                    card.style.display = 'flex';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}
    </script>
</body>
</html>
"""


def main():
    validate_dataset(LEADS_DATA)
    os.makedirs("demos", exist_ok=True)
    for lead in LEADS_DATA:
        folder = os.path.join("demos", lead["slug"])
        os.makedirs(folder, exist_ok=True)
        html_page = build_demo_html(lead)
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_page)

    dashboard_page = build_dashboard_html(LEADS_DATA)
    with open("dashboard.html", "w", encoding="utf-8") as f:
        f.write(dashboard_page)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(dashboard_page)

    print("🚀 SUCCESS: Generated 45 unique niche demos + index.html & dashboard.html!")


if __name__ == "__main__":
    main()
