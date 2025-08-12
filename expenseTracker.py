import matplotlib.pyplot as plt
expenses = []  
def menu():
    """
     This function displays all the functionalities that this application can do
    """
    print("1.add expense")
    print("2. view expenses")
    print("3. show expense total")
    print("4. view expense piechart")
  

    

def add_expenses():

    """
    This function asks the user to enter expenses and their amounts, storing them in a list of dictionaries.
    Each dictionary contains the expense's name and amount.
    Continues until the user enters 'done'.
    """
   
    while True:
        expense_category =input("Enter category eg. Food,rent,travel, Entertainment ")
        if expense_category.lower() == 'done':
            break
        while True:
                try:
                    amount= float(input(f"Enter the amount for '{expense_category}': R "))
                   
                    # Check if the amount is a positive number
                    if amount <= 0:
                        print("Amount must be a positive number. Please try again.")
                    else:
                    # Append a dictionary with the expense category and amount to the list
                        expenses.append({"expense_category": expense_category, "amount": amount})
                        break # Break the inner loop if the input is valid
                except ValueError:
                # Handle non-numeric input
                    print("Invalid input. Please enter a valid number.")
                
            
        # return expenses
    
    
def view_expenses():
    if not expenses:
        print("no expense recorded")
        return
    print("\n--- ALL EXPENSES---")
    for i, expense in enumerate(expenses,1):
        
        print(f"{i}. R{expense['amount']:.2f} - {expense['expense_category']}")
        
        
        
        
def total():
    total = sum(expense['amount'] for expense in expenses)
    
    # print(f"The total of all your expenses is R{total}:.2f")
    return total
    
    
    
def display_chart():
    
    """
    Generates a pie chart from the list of expense dictionaries using matplotlib.
    """
    # Check if there are any expenses to plot
    if not expenses:
        print("No expenses to plot.")
        return

    # Extract labels and sizes from the list of dictionaries
    labels = [expenseName['expense_category'] for expenseName in expenses]
    sizes = [amount['amount'] for amount in expenses]

    # Create the pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal') # Ensures the pie chart is a circle
    plt.title('Monthly Spending Breakdown')
    plt.show() # Display the chart
    
    
    
def main():
    """
    Main function to run the budget tracker application.
    """
    print("--- Welcome to the Simple Budget Tracker! ---")
    
    # This loop allows the user to perform multiple actions
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expenses()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            user_total = total()
            print(f"\nTotal Spending: R{user_total:.2f}")
        elif choice == '4':
            display_chart()
        else:
            print("Invalid choice. Please try again.")


    

if __name__ == "__main__":
    main()
