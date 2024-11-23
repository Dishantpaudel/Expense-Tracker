import json
expenses = []
expense1 = {'amount': '00.00', 'category': 'Lets start', 'description': 'Just for fun','date':'2024/12/01'}
expenses.append(expense1)


# Function to remove an expense
def removeexpenses():
    while True:
        listexpenses()  # Calling listExpenses to show current expenses
        print("Which expense should be removed? Please enter the index.")
        expenseToRemove = input(">")
        
        # being sure input is not empty or invalid
        if not expenseToRemove.strip():  # its checks  if input is empty or contains only spaces
            print("Invalid input. Please enter a valid index number.")
            continue
        
        try:
            expenseToRemove = int(expenseToRemove)  # Converting the input to an integer
            
            # Ensuring the index is within the valid range
            if 0 <= expenseToRemove < len(expenses):
                del expenses[expenseToRemove]  # Removing the expense by index
                print("Expense removed successfully!")
                break
            else:
                print("Invalid index. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to add a new expense
def addexpenses(amount, category, description="",date=""):
    expense = {'amount': amount,
               'category': category,
                'description': description,
                'date': date  }
    expenses.append(expense)  # Appends the new expense 
    print("Expense added successfully!")

# Function to list all expenses
def listexpenses():
    print("\nHere is a list of your expenses:")
    print("____________________")
    
    if not expenses:  # Checking if the list is empty
        print("No expenses to show.")
    else:
        for index, expense in enumerate(expenses):
            print(f"# {index} - Amount: {expense['amount']} - Category: {expense['category']} - Description: 
                {expense['description']} - Date: {expense['date']}")
    print("\n")
def display_totals_by_category():
    totals = {}
    for expense in expenses:
        category = expense['category']
        amount = float(expense['amount'])
        totals[category] = totals.get(category, 0) + amount

    print("\nTotals by Category:")
    for category, total in totals.items():
        print(f"{category}: {total:.2f}")
    print("\n")
# Saving expenses to a file
def save_expenses_to_file(filename="expenses.json"):
    with open(filename, "w") as file:  # Opening the file in write mode
        json.dump(expenses, file, indent=4)  # Writing in  the expenses list to the file in JSON format
    print(f"Expenses saved to {filename}.")    
# Loading expenses from a file
def load_expenses_from_file(filename="expenses.json"):
    global expenses  # Allowing modification of the global expenses list
    try:
        with open(filename, "r") as file:  # Opening  the file in read mode
            expenses = json.load(file)  # Reading and loading the data into the expenses list
        print(f"Expenses loaded from {filename}.")
    except FileNotFoundError:
        print(f"No saved data found. Starting fresh.")
    except json.JSONDecodeError:
        print(f"Corrupted data in {filename}. Starting fresh.")
    

# Function to display the menu
def printMenu():
    print("Please choose one from one of the following options:")
    print("1. Add a new expense")
    print("2. Remove an expense")
    print("3. List all expenses")
    print("4. Display totals by category")
    print("5. Exit")

# Main program loop
if __name__ == "__main__":
    load_expenses_from_file() 
    while True:
        printMenu()  # Display the menu
        optionSelected = input(">")
        
        if optionSelected == "1":  # Option to add a new expense
            print("How much was this expense?")
            amountToAdd = input(">")  # Get amount input from user
            
            print("Which category was this expense?")
            category = input(">")  # Get category input from user
            
            print("What is the description of the expenses")
            description = input(">")
            print("Write the expenses date")
            date= input(">")
            addexpenses(amountToAdd, category, description,date)  # Add the expense to the list
            
        elif optionSelected == "2":  # Option to remove an expense
            if not expenses:  # If there are no expenses, display a message
                print("No expenses to remove.")
            else:
                removeexpenses()  # Call the removeexpenses function to handle removal
                
        elif optionSelected == "3":  # Option to list all expenses
            listexpenses()
        # Display the list of expenses
        elif optionSelected =="4": 
            display_totals_by_category()
            
        elif optionSelected == "5":  # Option to exit the program
            save_expenses_to_file()
            print("Exiting the program. Goodbye!")
            break  # Exit the program
            
        else:
            print("Invalid input. Please select a valid option.")  # Handle invalid menu option
