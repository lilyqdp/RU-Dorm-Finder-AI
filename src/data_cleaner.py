def clean_and_encode(filepath="data/processed/machineinput_rutgers_dorms.csv"):
    """
    Reads the raw dorm CSV file, encodes Yes/No values as 1/0,
    removes duplicates, fills missing values, and saves a clean version.
    """
    try:
        df = pd.read_csv(filepath)

        # Example encoding (add columns as needed)
        yes_no_columns = ["AC", "WiFi", "Laundry", "Lounge", "Private_Bathroom"]
        for col in yes_no_columns:
            if col in df.columns:
                df[col] = df[col].map({"Yes": 1, "No": 0})

        df = df.drop_duplicates().fillna(0)
        df.to_csv("data/processed/machineinput_rutgers_dorms_encoded.csv", index=False)
        print("✅ Data successfully cleaned and encoded.")
        print(df.head())

    except FileNotFoundError:
        print("⚠️ File not found. Make sure 'rutgers_dorms.csv' exists in data/processed/.")
    except Exception as e:
        print(f"⚠️ Error cleaning data: {e}")