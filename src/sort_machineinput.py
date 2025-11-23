import pandas as pd
import re

def normalize(name: str):
    name = name.lower()
    name = re.sub(r'[^a-z0-9 ]', '', name)   # remove punctuation
    return name.strip()

def sort_machineinput():

    path = "data/processed/machineinput_rutgers_dorms.csv"
    df = pd.read_csv(path)

    desired_campus_order = [
        "Busch",
        "Livingston",
        "College Ave",
        "Cook/Douglass"
    ]

    # Create lookup map
    df["campus_rank"] = df["Campus"].apply(lambda c: desired_campus_order.index(c) if c in desired_campus_order else 999)

    # create normalized name field
    df["name_key"] = df["Dorm_Name"].apply(normalize)

    # sort by both
    df = df.sort_values(by=["campus_rank", "name_key"]).reset_index(drop=True)

    # clean artifacts
    df = df.drop(columns=["campus_rank", "name_key"])

    # overwrite file
    df.to_csv(path, index=False)

    print("🔥 machineinput correctly sorted by (campus → name)")
