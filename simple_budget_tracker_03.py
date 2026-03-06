# Monthly Budget Tracker with Multiple Expenses

print("===================================")
print("      Monthly Budget Tracker       ")
print("===================================\n")

# Step 1: Ask for total monthly budget
while True:
    budget_input = input("Enter your total monthly budget (LKR): ").strip()
    if budget_input == "":
        print("You must enter a value for the budget!")
        continue
    try:
        total_budget = float(budget_input)
        if total_budget < 0:
            print("Budget cannot be negative. Try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Step 2: Ask for expenses repeatedly
expenses = []
expense_count = 1
print("\nEnter your expenses one by one. Type 'done' when finished.")

while True:
    expense_input = input(f"Enter expense {expense_count} (LKR): ").strip()
    
    if expense_input.lower() == "done":
        if len(expenses) == 0:
            print("You must enter at least one expense before finishing.")
            continue
        else:
            break
    
    if expense_input == "":
        print("You must enter a value or type 'done' to finish!")
        continue
    
    try:
        expense = float(expense_input)
        if expense < 0:
            print("Expense cannot be negative. Try again.")
        else:
            expenses.append(expense)
            expense_count += 1
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'done'.")

# Step 3: Calculate remaining balance
total_expenses = sum(expenses)
remaining_balance = total_budget - total_expenses

# Step 4: Display formatted results
print("\n" + "-" * 40)
print(f"{'Total Budget':<25}: LKR {total_budget:.2f}")
for idx, exp in enumerate(expenses, start=1):
    print(f"Expense {idx:<20}: LKR {exp:.2f}")
print(f"{'Remaining Balance':<25}: LKR {remaining_balance:.2f}")
print("-" * 40)

# Step 5: Display messages based on balance
if remaining_balance < 0:
    print("You have exceeded your budget! Try to save next month. 💡")
elif remaining_balance < 500:
    print("Warning: Low Funds ⚠️")
elif remaining_balance == 0:
    print("You have perfectly balanced your budget! 🎯")
else:
    print("Good job! You have some money left over. 💰")
