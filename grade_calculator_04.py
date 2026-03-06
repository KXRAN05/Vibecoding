# Enhanced Grade Calculator with Clean Output

print("=============================================")
print("        Welcome to the Grade Calculator       ")
print("=============================================\n")

while True:
    # Step 0: Ask if user wants to continue
    while True:
        choice = input("Type 'yes' to calculate grades or 'quit' to exit: ").strip().lower()
        if choice == "":
            print("You must type something! Please type 'yes' or 'quit'.")
        elif choice in ["yes", "quit"]:
            break
        else:
            print("Invalid input! Please type 'yes' to calculate or 'quit' to exit.")

    if choice == "quit":
        print("\nThank you for using the Grade Calculator. Goodbye!")
        break

    # Step 1: Get user's name
    while True:
        name = input("\nEnter your name: ").strip()
        if name == "":
            print("You must type your name to continue!")
        else:
            break

    # Step 2: Get marks for 3 subjects
    marks = []
    for i in range(1, 4):
        while True:
            mark_input = input(f"Enter marks for subject {i} (0-100): ").strip()
            if mark_input == "":
                print("You must enter a mark!")
                continue
            try:
                mark = float(mark_input)
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a number between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    # Step 3: Calculate average
    average = sum(marks) / len(marks)

    # Step 4: Determine grade
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    # Step 5: Display clean, formatted output
    print("\n" + "-" * 30)
    print(f"{'Name':<10}: {name}")
    print(f"{'Average':<10}: {average:.2f}")
    print(f"{'Grade':<10}: {grade}")
    print("-" * 30)

    # Step 6: Motivational message if fail
    if grade == "Fail":
        print("Don't worry! Keep trying and you'll improve. 💪")
    print("\n")  # extra space before next loop
