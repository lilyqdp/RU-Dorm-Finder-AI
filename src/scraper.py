"""
scraper.py
Scrapes dorm and apartment names with their basic features for each Rutgers campus.

Author: Lily Del Pilar
"""

import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://ruoncampus.rutgers.edu"

def scrape_campus(campus_name, campus_url):
    print(f"\n📍 Scraping {campus_name} Campus...")
    data = []

    response = requests.get(campus_url)
    if response.status_code != 200:
        print(f"❌ Could not load {campus_url} (status {response.status_code})")
        return data

    soup = BeautifulSoup(response.text, "html.parser")
    dorm_links = []

    # Find dorm URLs on the campus page
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if f"/living-on-campus/{campus_url.split('/')[-1]}/" in href and href != campus_url:
            full_link = href if href.startswith("http") else BASE_URL + href
            dorm_links.append(full_link)

    dorm_links = list(set(dorm_links))
    print(f"Found {len(dorm_links)} dorm links for {campus_name}.\n")

    # Visit each dorm page and extract details
    for link in dorm_links:
        try:
            res = requests.get(link)
            if res.status_code != 200:
                print(f"Skipping {link} (status {res.status_code})")
                continue

            dorm_soup = BeautifulSoup(res.text, "html.parser")
            dorm_name_tag = dorm_soup.find("h1")
            dorm_name = dorm_name_tag.text.strip() if dorm_name_tag else "Unknown Dorm"

            features = [li.text.strip() for li in dorm_soup.find_all("li")]
            if not features:
                features = ["No listed features found"]

            data.append({
                "Campus": campus_name,
                "Dorm Name": dorm_name,
                "URL": link,
                "Features": ", ".join(features)
            })

            print(f"✅ {dorm_name} — {len(features)} features found.")
            time.sleep(1)

        except Exception as e:
            print(f"⚠️ Error processing {link}: {e}")
            continue

    return data
