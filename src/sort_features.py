import pandas as pd
import re

def sort_features(text):
    keywords = [
        "Type of Residence Hall",
        "Number of Students",
        "Number of Floors",
        "Average Room Size",
        "Availability",
        "Contract Type",
        "Elevator"
    ]
    try:
# "Type of Residence Hall: Traditional Hall Number of Students: 217 Number of Floors: 4 Average Room Size: 18x12 Availability: First-Year Students Contract Type: Undergraduate Academic Year (Two semesters) What's Nearby? Busch Dining Hall, Busch Student Center, Busch Recreation Bubble, Libraries Annex, Sonny Werblin Recreation Center (premier athletic facility), intramural fields. Features & Amenities Air-cooled* Vending machines Wifi throughout the building Laundry facility Building main lounge Floor lounges Pool table, table tennis, foosball table Communal bathrooms (separated by gender) *Students living in air-cooled halls are encouraged to review our moisture control resources . What's included in my space? What’s included in my room? Twin extra long bed and mattress Beds have the ability to be lofted Closet space Dresser Desk Chair Microfridge Blinds or curtains Wifi in bedrooms Carpeted flooring"
        extracted = {}
        extracted["Elevator"] = "No"
        remaining_lines = []
        for kw in keywords:

            # print("     trying " + kw)
            matched = False
            for line in text.splitlines():
                feat = line.strip()
                if feat.startswith(kw + ":"):
                    feat = feat.replace('"', '').replace(' Students', '').replace(' Student', '')
                    if kw == "Number of Students":
                        feat = feat.replace(',', '')
                    if kw == "Average Room Size":
                        feat = feat.replace(' ', '').replace('SquareFeet', '')


                    feat = re.sub(r'(\d+)x(\d+)', lambda m: str(int(m.group(1)) * int(m.group(2))), feat)
                    extracted[kw] = feat.split(":", 1)[1].strip()
                    matched = True
                    # print("Matched " + kw)
                    continue
                if "Elevator" in line:
                    # print("WOO YEAH BABY")
                    extracted["Elevator"] = "Yes"



        # print("🔥 sort done fire emoji")

        rename_map = {
                "Type of Residence Hall": "Type",
                "Number of Students": "Number_Students",
                "Number of Floors": "Floors",
                "Average Room Size": "Average_Room_Size",
                "Contract Type": "Contract_Type"
        }

        renamed_features = {rename_map.get(k, k): v for k, v in extracted.items()}
        return renamed_features

    except Exception as e:
        print("⚠️ SORT ERROR:", e)
