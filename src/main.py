"""
main.py
DormFinder AI
-------------
Main entry point that coordinates the data scraping, cleaning, and dorm recommendation system.

Author: Lily Del Pilar & Charley Yang
"""

import os
import time
import pandas as pd
from scraper import scrape_campus
from data_cleaner import clean_and_encode
from interface import run_interface
from fill_template import fill_template 

# -----------------------------------
# STEP 1: Define base URLs
# -----------------------------------
BASE_URL = "https://ruoncampus.rutgers.edu"
CAMPUS_PAGES = {
    "Busch": f"{BASE_URL}/living-on-campus/busch-campus",
    "College Ave": f"{BASE_URL}/living-on-campus/college-ave",
    "Cook/Douglass": f"{BASE_URL}/living-on-campus/cookdouglass",
    "Livingston": f"{BASE_URL}/living-on-campus/livingston"
}

# -----------------------------------
# STEP 2: Scrape all campuses
# -----------------------------------
def scrape_all_campuses():
    print("\n📡 Starting Rutgers Dorm Data Scraper...\n")
    all_data = []
    
    for campus_name, url in CAMPUS_PAGES.items():
        all_data.extend(scrape_campus(campus_name, url))
        time.sleep(1)

    scraped_df = pd.DataFrame(all_data)

    template_path = "data/raw/machineinput_rutgers_dorm_template.csv"
    df_template = pd.read_csv(template_path)

    df_template["Dorm_Name"] = scraped_df["Dorm_Name"]
    df_template["Campus"] = scraped_df["Campus"]

    save_path = "data/processed/rutgers_dorms.csv"
    os.makedirs("data/processed", exist_ok=True)
    df_template.to_csv(save_path, index=False)

    print("\n🎉 Template successfully updated (Dorm_Name + Campus)!")
    print(f"Saved to: {save_path}")
    print("\nPreview:")
    print(df_template.head())

    return df_template


# -----------------------------------
# STEP 3: Program Menu
# -----------------------------------
def main():
    while True:
        print("\n=== DormFinder AI ===")
        print("1. Scrape Dorm Data")
        print("2. Clean & Encode Data")
        print("3. Run Dorm Search")
        print("4. Fill Template (Dorms + Campus)")
        print("5. Exit")
        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            scrape_all_campuses()
        elif choice == "2":
            clean_and_encode()
        elif choice == "3":
            run_interface()
        elif choice == "4":
            fill_template()
        elif choice == "5":
            print("👋 Exiting DormFinder AI. Goodbye!")
            break
        else:
            print("⚠️ Invalid selection. Please choose a valid option (1–5).")


if __name__ == "__main__":
    main()
