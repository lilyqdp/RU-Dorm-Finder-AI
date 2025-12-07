import pandas as pd
import re
from sort_features import sort_features

def normalize(name: str):
    name = name.lower()
    name = re.sub(r'[^a-z0-9 ]', '', name)   # remove punctuation
    return name.strip()

def sort_machineinput():

    path = "data/processed/scraped_data.csv"
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

    # SORT FEATURES
    # print(df["Features"].apply(sort_features))
    df_features = (df["Features"].apply(sort_features)).apply(pd.Series)
    df = pd.concat([df.drop(columns=["Features"]), df_features], axis=1)

    # write to file
    newpath = "data/processed/machineinput_rutgers_dorms.csv"
    df.to_csv(newpath, index=False)

    print("🔥 machineinput correctly sorted by (campus → name)")
