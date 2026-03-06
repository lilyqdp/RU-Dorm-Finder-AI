from parser import search_nlp
import os

path = "data/processed/merge_data.csv"

def run_interface():
    print("Welcome to DormFinder AI!")
    print("Type your query in natural language or '/help' to see a list of suggested categories. \nUse '/results' to change the number of displayed results.")
    n = 10

    while True:

        if os.path.getsize(path) == 0:

            print("\n⚠️  No data! Try '3. Merge Data' first.")
            return None
        user_input = input("\nEnter your query or 'quit' to exit: ").strip()
        if user_input in ['quit', 'exit']:
            break
        if user_input in ['/help']:
            print("Campus, Dorm Name, Housing Type, Year Availability, AC, Bathroom/Kitchen type, Elevator access, Open during breaks")
            continue
        if user_input in['/results']:
                n_input = input("\nEnter the number of results you want displayed (default: 10): ").strip()
                try:
                    n = int(n_input)
                except ValueError:
                    print("Invalid number. Using default: 10.")
                    n = 10
                continue

        
        results = search_nlp(user_input, n)

        print(f"\nTop {n} matches:\n")
        for i, row in results.iterrows():
            if row['similarity'] == 0:
                print("No more valid results.")
                break
            print(f"{i+1}:")
            print(f"{row['Dorm_Name']} ({row['Campus']} {row['Type']}) -- Similarity: {row['similarity']:.3f}")
            print(f"Number of students: {row['Number_Students']} || Floors: {row['Floors']:.0f} || Average Room Size: {row['Average_Room_Size']:.2f} square feet")
            print(f"Open to: {row['Availability']} Students || Room Style: {row['Room_Style']} || AC: {row['AC']} || Elevator: {row['Elevator']}")
            print(f"Bathroom: {row['Bathroom']} || Kitchen: {row['Kitchen']} || Occupancy: {row['Occupancy']:.0f} || Open During Breaks: {row['Open_During_Breaks']}")
            print(f"URL: {row['URL']}\n")
