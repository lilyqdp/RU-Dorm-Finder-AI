import pandas as pd

def fill_template():

    scraped = "data/processed/machineinput_rutgers_dorms.csv"
    template = "data/processed/filled_template.csv"
    out = "data/processed/filled_template.csv"

    try:
        df_scraped = pd.read_csv(scraped)
        df_template = pd.read_csv(template)

        # normalize keys for match
        df_scraped["key"] = df_scraped["Dorm_Name"].str.lower().str.replace(r'[^a-z0-9]', '', regex=True)
        df_template["key"] = df_template["Dorm_Name"].str.lower().str.replace(r'[^a-z0-9]', '', regex=True)


        # merge left ON THE TEMPLATE
        merged = df_template.merge(
            df_scraped,
            on="key",
            how="left",
            suffixes=("_template", "_scraped")
        )

        # copy these columns from scraped into template
        cols = ["Campus", "Type", "Occupancy", "Room_Style", "A/C", "Bathroom", "Kitchen", "Gym", "URL"]

        for col in cols:
            merged[col + "_template"] = merged[col + "_scraped"]

        final = merged[[c+"_template" for c in cols]]
        final.columns = cols

        df_template[cols] = final[cols]
        df_template = df_template[df_template["Dorm_Name"] != "Marvin Apartments"].reset_index(drop=True)
        df_template.to_csv(out, index=False)

        print("🔥 Template filled using NAME matching (not by row number)")

    except Exception as e:
        print(f"⚠️ ERROR: {e}")
