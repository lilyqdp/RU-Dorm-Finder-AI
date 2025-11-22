import pandas as pd

def fill_template(
        scraped="data/processed/rutgers_dorms.csv",
        template="data/raw/machineinput_rutgers_dorm_template.csv",
        out="data/processed/rutgers_dorms_filled.csv"
    ):
    
    try:
        df_scraped = pd.read_csv(scraped)
        df_template = pd.read_csv(template)

        # rename scraped
        df_scraped = df_scraped.rename(columns={"Dorm Name": "Dorm_Name"})

        # reduce to 2 columns
        df_scraped = df_scraped[["Dorm_Name", "Campus"]]

        # write into template
        df_template["Dorm_Name"] = df_scraped["Dorm_Name"]
        df_template["Campus"] = df_scraped["Campus"]

        df_template.to_csv(out, index=False)
        print(f"✅ Template filled successfully → {out}")

    except Exception as e:
        print(f"⚠️ ERROR: {e}")
