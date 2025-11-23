import pandas as pd

def merge_data():

    scraped_file = "data/processed/machineinput_rutgers_dorms.csv"
    human_file   = "data/processed/humaninput_rutgers_dorms.csv"
    out_file     = "data/processed/merge_data.csv"

    try:
        df_scraped = pd.read_csv(scraped_file)
        df_human = pd.read_csv(human_file)

        df_scraped = df_scraped[["Dorm_Name", "Campus"]]
        df_filtered = df_human.merge(df_scraped, on=["Dorm_Name", "Campus"])
        
        df_filtered.to_csv(out_file, index=False)

        print("🔥 merge done → only matching rows preserved")
        print(f"Saved: {out_file}")

    except Exception as e:
        print("⚠️ MERGE ERROR:", e)
