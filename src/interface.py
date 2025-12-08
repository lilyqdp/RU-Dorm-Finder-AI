from parser import search_nlp

def run_interface():
    print("Welcome to DormFinder AI!")
    print("Type your query in natural language or 'help' to see a list of suggested categories.")
    
    while True:
        n = 5
        user_input = input("\nEnter your query or 'quit' to exit: ").strip()
        if user_input in ['quit', 'exit']:
            break
        if user_input in ['help']:
            print("Campus, Dorm Name, Housing Type, Year Availability, AC, Bathroom/Kitchen type, Elevator access, Open during breaks")
            continue

        
        results = search_nlp(user_input)

        print(f"\nTop {n} matches:\n")
        for i, row in results.iterrows():
            print(f"{row['Dorm_Name']} ({row['Campus']}) -- Similarity: {row['similarity']:.3f}")
            print(f"Number of students: {row['Number_Students']} || Floors: {row['Floors']:.0f} || Average Room Size: {row['Average_Room_Size']} square feet")
            print(f"Open to: {row['Availability']} Students || Room Style: {row['Room_Style']} || AC: {row['AC']} || Elevator: {row['Elevator']}")
            print(f"Bathroom: {row['Bathroom']} || Kitchen: {row['Kitchen']} || Occupancy: {row['Occupancy']:.0f} || Open During Breaks: {row['Open_During_Breaks']}")
            print(f"URL: {row['URL']}\n")
