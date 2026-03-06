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
        extracted = {}
        extracted["Elevator"] = "No"
        remaining_lines = []
        for kw in keywords:

            # print("     trying " + kw)
            matched = False
            for line in text.splitlines():
                feat = line.strip()
                if feat.startswith(kw + ":"):
                    # removes inconsistent '"' in "Average Room Size" and extra "Student/Students" in "Availability"
                    feat = feat.replace('"', '').replace(' Students', '').replace(' Student', '')
                    # removes thousands separator comma in Number of Students
                    if kw == "Number of Students":
                        feat = feat.replace(',', '')
                    # removes inconsistent SquareFeet usage in Room Size to make it consistent
                    if kw == "Average Room Size":
                        feat = feat.replace(' ', '').replace('SquareFeet', '')
                    # finds the first number in Number of Floors and uses that as the number of floors -- some have values like "Up to 7" which becomes just 7
                    if kw == "Number of Floors":
                        first_number = re.search(r"\d+", feat)
                        extracted[kw] = first_number.group() if first_number else None
                        matched = True
                        continue
                    # regex that identifies when the average room size shows dimensions rather than square feet, then converts to square feet to make consistent.
                    
                    feat = re.sub(r'(\d+)x(\d+)', lambda m: str(int(m.group(1)) * int(m.group(2))), feat)
                    extracted[kw] = feat.split(":", 1)[1].strip()
                    matched = True
                    # print("Matched " + kw)
                    continue

                # if Elevator is mentioned set elevator attribute to yes
                if "Elevator" in line:
                    # print("yippe")
                    extracted["Elevator"] = "Yes"



        # print("🔥 sort done")

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
