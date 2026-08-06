"""
    Expense Tracker Application
    This application allows users to track their expenses by adding them with a category and description. 
    It provides functionality to view all expenses, calculate totals by category, find the largest expense, 
    and get a summary of spending by category.
    
Classes:
    ExpenseTracker: Manages a collection of expenses with various operations.
    
Methods:
    add_expense(amount, category, description): Adds a new expense to the tracker.
    get_all_expenses(): Returns a list of all expenses.
    get_total_by_category(category): Returns the total amount spent in a specific category.
    get_largest_expense(): Returns the largest expense recorded.
    get_category_summary(): Returns a summary of total spending by category.

"""
class ExpenseTracker:
    def __init__(self):
        """
        Initialize an empty list to store expenses. 
        Each expense is a dictionary with keys 'amount', 'category', and 'description'.
        """
        self.expenses = []
    
    def __str__(self):
        """ String representation of the expense tracker for easy viewing """
        result = "=== Expense Tracker ===\n"
        expense_counter = 0
        for expense in self.expenses:
            expense_counter += 1
            result += f"{expense_counter}. {expense['category']}: ${expense['amount']}: {expense['description']}\n"
        result += f"Total: ${sum(expense['amount'] for expense in self.expenses)}\n"
        """ !!!
        The above line uses a generator expression to calculate the total amount of all expenses by summing the 'amount' field 
        of each expense in the self.expenses list. This is an efficient way to calculate the total without needing to 
        create an intermediate list of amounts, as the generator expression computes each amount on-the-fly during the 
        summation process. More efficient for large datasets as it avoids creating an additional list in memory.
        """
        result += "======================="
        return result

    def add_expense(self, amount, category, description):
        """
        Add expense to expenses list

        Args:
            amount (int or float): The amount of the expense.
            category (str): The category of the expense.
            description (str): A description of the expense.

        Returns:
            bool: True if the expense was added successfully, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False
        if not isinstance(category, str) or not category.strip():
            return False
        if not isinstance(description, str) or not description.strip():
            return False
        
        self.expenses.append({
            'amount': round(amount, 2),  # Round to 2 decimal places for currency
            'category': category.lower(),  # Normalize category to lowercase for consistency
            'description': description
        })
        return True

    def get_all_expenses(self):
        """
        Get a list of all expenses.

        Returns:
            list: A list of all expenses.
        """
        return self.expenses

    def get_total_by_category(self, category):
        """
        Sum the total amount spent in a specific category.

        Args:
            category (str): The category to calculate the total for.

        Returns:
            float: The total amount spent in the specified category.
        """
        if not isinstance(category, str) or not category.strip():
            return 0
        category = category.lower()  # Normalize category for case-insensitive comparison
        total = 0.0     # Float accumulator for total amount in the specified category
        # The Accumulator Pattern (Summing)
        for expense in self.expenses:
            if expense['category'].lower() == category:
                total += expense['amount']
        return total

    def get_largest_expense(self):
        """
        Find the largest expense in the tracker. 
        
        Returns:
            dict: The largest expense with keys 'amount', 'category', and 'description'. 
            Returns None if there are no expenses.
        """
        if not self.expenses:
            return None
        largest = max(self.expenses, key=lambda x: x['amount'])
        return largest
    
    def get_category_summary(self):
        """ 
        Get a summary of total spending by category.
        
        Returns:
            dict: A dictionary where keys are categories (lowercase) and values are total amounts spent in those categories.
        """
        summary = {}
        for expense in self.expenses:
            category = expense['category'].lower()  # Normalize category for case-insensitive comparison
            summary[category] = summary.get(category, 0) + expense['amount']
        return summary

if __name__ == "__main__":
    """
    Example usage of the ExpenseTracker class. 
    This block will only run if the script is executed directly, and not when imported as a module.
    It demonstrates adding expenses, viewing all expenses, calculating totals by category, finding the largest expense, 
        and getting a summary of spending by category.
    """
    # Example usage:
    tracker = ExpenseTracker()
    # Add expenses
    tracker.add_expense(15.50, "Food", "Lunch at cafe")
    tracker.add_expense(8.00, "Food", "Morning coffee")
    tracker.add_expense(30.00, "Transport", "Taxi to airport")
    tracker.add_expense(12.00, "Entertainment", "Movie ticket")
    tracker.add_expense(50.00, "Food", "Groceries")

    # View all
    print("All expenses:")
    for expense in tracker.get_all_expenses():
        print(f"  {expense}")

    # Category total
    print(f"\nFood spending: ${tracker.get_total_by_category('Food')}")

    # Largest expense
    print(f"\nLargest expense: {tracker.get_largest_expense()}")

    # Summary by category
    print("\nSpending by category:")
    for category, total in tracker.get_category_summary().items():
        print(f"  {category}: ${total}")

    # Pretty print this object using the __str__ method
    print("\n")
    print(tracker)