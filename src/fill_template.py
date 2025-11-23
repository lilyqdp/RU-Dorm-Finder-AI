import pandas as pd

def fill_template():

    scraped = "data/processed/machineinput_rutgers_dorms.csv"
    template = "data/processed/filled_template.csv"
    out = "data/processed/filled_template.csv"

    try:
        df_scraped = pd.read_csv(scraped)
        df_template = pd.read_csv(template)

        # ensure length matches
        if len(df_scraped) != len(df_template):
            print("⚠️ Template rows ≠ scraped rows")
            print("⚠️ Will only fill matching rows in order")

        n = min(len(df_scraped), len(df_template))

        df_template.loc[:n-1, "Dorm_Name"] = df_scraped.loc[:n-1, "Dorm_Name"]
        df_template.loc[:n-1, "Campus"] = df_scraped.loc[:n-1, "Campus"]

        df_template.to_csv(out, index=False)

        print(f"🔥 Template updated successfully → {out}")

    except Exception as e:
        print(f"⚠️ ERROR: {e}")
