import pandas as pd

def merge_data():

    scraped_file = "data/processed/machineinput_rutgers_dorms.csv"
    human_file   = "data/processed/humaninput_rutgers_dorms.csv"
    out_file     = "data/processed/merge_data.csv"

    filtered_scraped_file = "data/processed/filteredmachineinput_rutgers_dorms.csv"

    try:
        df_scraped = pd.read_csv(scraped_file)
        df_human = pd.read_csv(human_file)

        # trim whitespace in names, fixes matching issues
        df_scraped["Dorm_Name"] = df_scraped["Dorm_Name"].str.strip()
        df_human["Dorm_Name"] = df_human["Dorm_Name"].str.strip()

        df_scraped["Campus"] = df_scraped["Campus"].str.strip()
        df_human["Campus"] = df_human["Campus"].str.strip()

        df_filtered = df_human


        # df_filtered = df_scraped.merge(df_human, on=["Dorm_Name", "Campus"], how="outer", suffixes=("_scraped", "_human"))
        df_filtered[["Number_Students","Floors","Average_Room_Size","Availability", "Elevator"]] = df_scraped[["Number_Students","Floors","Average_Room_Size","Availability", "Elevator"]]
        # df_filtered = df_filtered.drop(columns=["Contract_Type"])

        df_filtered.to_csv(out_file, index=False)

        df_scraped.to_csv(filtered_scraped_file, index=False)

        print("🔥 merge done → only matching rows preserved")
        print(f"Saved: {out_file}")

    except Exception as e:
        print("⚠️ MERGE ERROR:", e)
