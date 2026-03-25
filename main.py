from agents.main_agent import route_task

def main():
    print("Welcome to StudyMate AI! 📚")
    print("Type your text and include keywords like 'summarize', 'question', or just ask a topic for a simple explanation.")
    print("Enter 'quit' or 'exit' to stop.\n" + "-" * 60)
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower().strip() in ['quit', 'exit']:
            print("Goodbye!")
            break
        
        print(f"\nStudyMate AI:\n{route_task(user_input)}")

if __name__ == "__main__":
    main()