import pandas as pd

def merge_data():

    scraped_file = "data/processed/machineinput_rutgers_dorms.csv"
    human_file   = "data/processed/humaninput_rutgers_dorms.csv"
    out_file     = "data/processed/merge_data.csv"

    try:
        df_scraped = pd.read_csv(scraped_file)
        df_human = pd.read_csv(human_file)

        # trim whitespace in names, fixes matching issues
        df_scraped["Dorm_Name"] = df_scraped["Dorm_Name"].str.strip()
        df_human["Dorm_Name"] = df_human["Dorm_Name"].str.strip()

        df_scraped["Campus"] = df_scraped["Campus"].str.strip()
        df_human["Campus"] = df_human["Campus"].str.strip()

        # keep ONLY name + campus from scraped
        df_scraped = df_scraped[["Dorm_Name", "Campus"]]

        # merge to keep only rows that exist in both
        df_filtered = df_human.merge(df_scraped, on=["Dorm_Name", "Campus"])

        df_filtered.to_csv(out_file, index=False)

        print("🔥 merge done → only matching rows preserved")
        print(f"Saved: {out_file}")

    except Exception as e:
        print("⚠️ MERGE ERROR:", e)
