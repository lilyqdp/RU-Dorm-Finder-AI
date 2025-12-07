from src.parser import *
# x = parse_query("busch double")
# print(x)
# y = query_to_vector(x)
# print(y)

# z = get_ranked_results("two person busch dorm ")
# print(z)

scraped_file = "data/processed/machineinput_rutgers_dorms.csv"
df_scraped = pd.read_csv(scraped_file)
print(df_scraped.loc[1, "Features"])