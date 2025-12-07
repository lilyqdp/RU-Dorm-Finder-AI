import os
import time
import pandas as pd
from src.scraper import scrape_campus
from src.interface import run_interface
from src.sort_machineinput import sort_machineinput
from src.merge_data import merge_data

BASE_URL = "https://ruoncampus.rutgers.edu"
CAMPUS_PAGES = {
    "Busch": f"{BASE_URL}/living-on-campus/busch-campus",
    "College Ave": f"{BASE_URL}/living-on-campus/college-ave",
    "Cook/Douglass": f"{BASE_URL}/living-on-campus/cookdouglass",
    "Livingston": f"{BASE_URL}/living-on-campus/livingston"
}

def scrape_all_campuses():
    print("\n📡 Starting Rutgers Dorm Data Scraper...\n")
    all_data = []
    
    for campus_name, url in CAMPUS_PAGES.items():
        all_data.extend(scrape_campus(campus_name, url))
        time.sleep(1)

    scraped_df = pd.DataFrame(all_data)

    os.makedirs("data/processed", exist_ok=True)

    save_path = "data/processed/machineinput_rutgers_dorms.csv"
    scraped_df.to_csv(save_path, index=False)

    print("\n🎉 Scrape complete!")
    print(f"Saved to: {save_path}")
    print("\nPreview:")
    print(scraped_df.head())

    return scraped_df

def scrape_a_campus():
    print("\n📡 Starting Rutgers Dorm Data Scraper...\n")
    all_data = []
    
    for campus_name, url in CAMPUS_PAGES.items():
        all_data.extend(scrape_campus(campus_name, url))
        time.sleep(1)

    scraped_df = pd.DataFrame(all_data)

    os.makedirs("data/processed", exist_ok=True)

    save_path = "data/processed/machineinput_rutgers_dorms.csv"
    scraped_df.to_csv(save_path, index=False)

    print("\n🎉 Scrape complete!")
    print(f"Saved to: {save_path}")
    print("\nPreview:")
    print(scraped_df.head())

    return scraped_df

def main():
    while True:

        scrape_a_campus()

        break



if __name__ == "__main__":
    main()