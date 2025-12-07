import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/processed/merge_data.csv")

# print(df.columns)
# exit()

categorical_cols = ["Campus", "Type", "Occupancy"]
# numeric_cols = ["Occupancy"]      //for numeric categories

encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X_cat = encoder.fit_transform(df[categorical_cols])

# X_num = df[numeric_cols].to_numpy()  

# X = np.hstack([X_cat, X_num])



def parse_query(query):
    query = query.lower()

    q = {
        "Campus": "Unknown",
        "Type": "Unknown",
        "Occupancy": "Unknown"
    }

    if "busch" in query: q["Campus"] = "Busch"
    if "livi" in query: q["Campus"] = "Livingston"
    if "cook" in query or "doug" in query: q["Campus"] = "Cook/Douglass"
    if "college" in query: q["Campus"] = "College Ave"

    if "apartment" in query: q["Type"] = "Apartment"
    if "dorm" in query: q["Type"] = "Dorm"

    if "four" in query or "4" in query: q["Occupancy"] = "4"
    if "two" in query or "2" in query: q["Occupancy"] = "2"

    print(q)

    return q

def query_to_vector(parsed):
    temp_df = pd.DataFrame([parsed])
    query_cat = encoder.transform(temp_df[categorical_cols])
    # query_num = temp_df[numeric_cols].to_numpy()
    return query_cat

def get_ranked_results(query):
    parsed = parse_query(query)
    query_vector = query_to_vector(parsed)
    similarity = cosine_similarity(query_vector, X_cat)[0]

    df["similarity"] = similarity
    return df.sort_values("similarity", ascending=False)