import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# insert any query term replacements here
term_map = {
    "-": " ",

    "college avenue": "CampusCollege Ave",
    "livingston": "CampusLivingston",
    "busch": "CampusBusch",
    "cook": "c/d",
    "douglass": "c/d",
    "doug": "c/d",
    "c/d": "CampusCook/Douglass",

    "air conditioning": "ACYes",
    " ac ": " ACYes ",

    "apartments": "TypeApartment",
    "residence hall": "TypeDorm",
    "dorms": "TypeDorm",
    
    "two person": "double",
    "single": "RoomStylesingle",
    "double": "RoomStyledouble",

    "first year": "First-year",
    "freshmen": "First-year",
    
    "elevators": "elevator",
    "elevator": "ElevatorYes",
    
    "private kitchen": "KitchenYes",
    "communal kitchen": "KitchenCommunal",
    "kitchen": "KitchenYes",

    "bathrooms": "bathroom",
    "private bathroom": "BathroomPrivate",
    "communal bathroom": "BathroomCommunal",
    
    "breaks": "break",
    "open during break": "BreakYes",
    "closed during break": "BreakNo"

    
}



def load():
    global df, vectorizer, categorical_cols, numerical_cols, feature_df, preprocess, feature_matrix, text_matrix

    
    df = pd.read_csv("data/processed/merge_data.csv")
    # creating description col and what each value means
    df['description'] = df.apply(
        lambda row: f"Campus{row['Campus']} {row['Dorm_Name']} Type{row['Type']} "
                    f"RoomStyle{row['Room_Style']} AC{row['AC']} Bathroom{row['Bathroom']} "
                    f"Kitchen{row['Kitchen']} Elevator{row['Elevator']} Break{row['Open_During_Breaks']}", axis=1
    )
    vectorizer = TfidfVectorizer(lowercase=True)
    text_matrix = vectorizer.fit_transform(df['description'])

    categorical_cols = ["Campus", "Dorm_Name", "Type", "Availability", "Room_Style", "AC", "Bathroom", "Kitchen", "Elevator", "Open_During_Breaks"]
    numerical_cols = ["Number_Students", "Floors", "Average_Room_Size", "Occupancy"]
    df[categorical_cols] = df[categorical_cols].astype('string')

    for col in numerical_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df[categorical_cols] = df[categorical_cols].fillna("Unknown")
    # replace unknowns with mean so they dont impact results
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())
    feature_df = df[categorical_cols + numerical_cols]
    preprocess = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", StandardScaler(), numerical_cols)

    ])

    X = preprocess.fit_transform(feature_df)
    feature_matrix = X.toarray()


def encode_query(query_dict, top_k=5):
    q = pd.DataFrame([ {col: None for col in feature_df.columns}])
    q[categorical_cols] = q[categorical_cols].astype('string')
    q[numerical_cols] = q[numerical_cols].astype("float64")

    
    for key, val in query_dict.items():
        if key in q.columns:
            q.at[0, key] = val

    for col in categorical_cols:
        q[col] = q[col].fillna("Unknown")

    for col in numerical_cols:
        q[col] = q[col].fillna(df[col].mean())

    q_vec = preprocess.transform(q).toarray()
    return q_vec


def search(query_dict, top_k=5):

    q_vec = encode_query(query_dict, top_k=top_k)
    sim = cosine_similarity(q_vec, feature_matrix)[0]
    idx = np.argsort(sim)[::-1][:top_k]
    results = df.iloc[idx].assign(similarity=sim[idx])
    return results

# basic nlp search
def encode_query_nlp(query):
    # convert to numeric vector
    return vectorizer.transform([query])

def preprocess_query(query):
    query = query.lower()

    # query term replacement - edit term_map
    for term, replacement in term_map.items():
        query = query.replace(term, replacement)

    return query

def search_nlp(query, top_k=5):

    load()


    query = preprocess_query(query)
    print(f"Keywords: {query}")
    # print(matched_keywords(query, df))
    q_vec = encode_query_nlp(query)
    sim = cosine_similarity(q_vec, text_matrix).flatten()

    idx = np.argsort(sim)[::-1][:top_k]
    similarityscore = df.iloc[idx].copy()
    similarityscore['similarity'] = sim[idx]



    bonus = 0
    # optional bonus for exact match, buggy
    # bonus = exact_match_bonus(query.lower(), df, weight=1.0)
    final_score = sim + bonus
    idx = np.argsort(final_score)[::-1][:top_k]
    results = df.iloc[idx].copy()
    results['score'] = final_score[idx]
    results = results.merge(similarityscore, how="left")
    return results

# rewards exact matches
def exact_match_bonus(query, df, weight=1.0):
    query_tokens = query.split()


    # print(matched_keywords(query, df))

    bonus = np.zeros(len(df))
    for token in query_tokens:
        bonus += df['description'].str.contains(token, case=False, regex=False).astype(float)
    return bonus * weight

# for testing which keywords were matched
def matched_keywords(query, df):
    
    query_tokens = query.split()
    # print(query_tokens)
    matched = []
    for idx, desc in enumerate(df['description']):
        desc_lower = desc.lower()
        matched_tokens = [token for token in query_tokens if token in desc_lower]
        if matched_tokens:
            matched.append((df.iloc[idx]['Dorm_Name'], matched_tokens))
    return matched