import csv
import json
import time
from urllib.parse import quote
from urllib.request import Request, urlopen

INPUT_CSV = "rutgers_dorm_addresses_for_geocoding.csv"
OUTPUT_CSV = "rutgers_dorm_coordinates.csv"

def geocode(address: str):
    url = f"https://nominatim.openstreetmap.org/search?q={quote(address)}&format=jsonv2&limit=1"
    req = Request(url, headers={"User-Agent": "DormFinderRutgers/1.0 (student project)"})
    with urlopen(req, timeout=30) as response:
        data = json.load(response)
    if not data:
        return "", ""
    return data[0].get("lat", ""), data[0].get("lon", "")

rows = []
with open(INPUT_CSV, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        lat, lon = geocode(row["Address"])
        row["Latitude"] = lat
        row["Longitude"] = lon
        rows.append(row)
        print(f'Geocoded: {row["Dorm_Name"]} -> {lat}, {lon}')
        time.sleep(1.1)  # be polite to the free service

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Dorm_Name","Campus","Address","Latitude","Longitude"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Saved {OUTPUT_CSV}")
