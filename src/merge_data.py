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

        # drop unused columns
        df_scraped = df_scraped.drop(columns=["URL","Type","Contract_Type"])

        # merge, keeps all columns from both df -- main purpose is to maintain row order of df_human
        df_filtered = df_scraped.merge(df_human, on=["Dorm_Name", "Campus"], how="right", suffixes=("_scraped", ""))

        # fill in empty column and remove duplicate
        df_filtered[["Number_Students","Floors","Average_Room_Size","Availability", "Elevator"]] = df_filtered[["Number_Students_scraped","Floors_scraped","Average_Room_Size_scraped","Availability_scraped", "Elevator_scraped"]]
        df_filtered = df_filtered.drop(columns=["Number_Students_scraped","Floors_scraped","Average_Room_Size_scraped","Availability_scraped", "Elevator_scraped"])


        df_filtered.to_csv(out_file, index=False)

        df_scraped.to_csv(filtered_scraped_file, index=False)

        print("🔥 merge done → only matching rows preserved")
        print(f"Saved: {out_file}")

    except Exception as e:
        print("⚠️ MERGE ERROR:", e)
