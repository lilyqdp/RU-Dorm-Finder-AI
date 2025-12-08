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
                    feat = feat.replace('"', '').replace(' Students', '').replace(' Student', '')
                    if kw == "Number of Students":
                        feat = feat.replace(',', '')
                    if kw == "Average Room Size":
                        feat = feat.replace(' ', '').replace('SquareFeet', '')
                    if kw == "Number of Floors":
                        first_number = re.search(r"\d+", feat)
                        extracted[kw] = first_number.group() if first_number else None
                        matched = True
                        continue

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
