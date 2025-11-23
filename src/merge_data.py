import pandas as pd

def merge_data():
    machine_file = "data/processed/machineinput_rutgers_dorms.csv"
    human_file   = "data/processed/humaninput_rutgers_dorms.csv"
    out_file     = "data/processed/merge_data.csv"

    try:
        df_machine = pd.read_csv(machine_file)
        df_human   = pd.read_csv(human_file)

        # merge ONLY on Dorm_Name + Campus
        df_merged = df_machine.merge(
            df_human,
            on=["Dorm_Name", "Campus"],
            how="inner"
        )

        df_merged.to_csv(out_file, index=False)

        print("\n🔥 Merge COMPLETE")
        print(f"✔️ Saved → {out_file}")
        print(df_merged.head())

    except Exception as e:
        print(f"⚠️ MERGE ERROR: {e}")
