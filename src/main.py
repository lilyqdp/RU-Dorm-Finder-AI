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
        time.sleep(2)  # polite delay between campus requests

    df = pd.DataFrame(all_data)
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/rutgers_dorms.csv", index=False, encoding="utf-8")

    print("\n✅ Scraping complete! Data saved to 'data/processed/rutgers_dorms.csv'")
    print("\nPreview of dataset:")
    print(df.head(5))
    return df


# -----------------------------------
# STEP 3: Program Menu
# -----------------------------------
def main():
    while True:
        print("\n=== DormFinder AI ===")
        print("1. Scrape Dorm Data")
        print("2. Clean & Encode Data")
        print("3. Run Dorm Search")
        print("4. Exit")
        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            scrape_all_campuses()
        elif choice == "2":
            clean_and_encode()
        elif choice == "3":
            run_interface()
        elif choice == "4":
            print("👋 Exiting DormFinder AI. Goodbye!")
            break
        else:
            print("⚠️ Invalid selection. Please choose a valid option (1–4).")


if __name__ == "__main__":
    main()
