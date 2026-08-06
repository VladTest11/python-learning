class BankAccount:
    """Base class for all bank accounts."""
    
    def __init__(self, account_number, holder_name, balance=0.0):
        """
        Initialize a bank account.
        
        Args:
            account_number (str): Unique account identifier
            holder_name (str): Name of account holder
            balance (float): Initial balance (default 0)
        """
        # Instance variables (protected with leading underscore convention)
        self._account_number = account_number
        self._holder_name = holder_name
        self._balance = balance
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit. Must be positive.
        
        Returns:
            bool: True if deposit was successful, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False
        self._balance += amount
        return True
    
    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (float): The amount to withdraw. Must be positive and not exceed the balance.

        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False
        if amount > self._balance:
            return False
        self._balance -= amount
        return True
    
    def get_balance(self):
        """
        Get the current balance of the account.

        Returns:
            float: The current balance.
        """
        return self._balance
    
    def get_account_info(self):
        """
        Get a dictionary representation of the account information.

        Returns:
            dict: A dictionary containing the account number, holder name, and balance.
        """
        return {
            "account_number": self._account_number,
            "holder_name": self._holder_name,
            "balance": self._balance
        }
        
    def __str__(self):
        """
        Return a string representation of the bank account.

        Returns:
            str: A string containing the account number, holder name, and balance.
        """
        return f"Account: {self._account_number} | Holder: {self._holder_name} | Balance: ${self._balance:.2f}"

class SavingsAccount(BankAccount):
    """Savings account with interest."""
    
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.02):
        """
        Initialize savings account.
        
        Args:
            account_number (str): Account ID
            holder_name (str): Holder name
            balance (float): Initial balance
            interest_rate (float): Annual interest rate (default 2% = 0.02)
        """
        # Call parent class constructor using super()
        super().__init__(account_number, holder_name, balance)
        self._interest_rate = interest_rate
        
    def apply_interest(self):
        """
        Apply interest to the current balance.
        
        Returns:
            float: The new balance after applying interest.
        """
        interest = self._balance * self._interest_rate
        self._balance += interest
        return interest

class CheckingAccount(BankAccount):
    """Checking account with transaction fee."""
    
    def __init__(self, account_number, holder_name, balance=0, transaction_fee=1.0):
        """
        Initialize checking account.
        
        Args:
            account_number (str): Account ID
            holder_name (str): Holder name  
            balance (float): Initial balance
            transaction_fee (float): Fee per withdrawal (default $1.00)
        """
        super().__init__(account_number, holder_name, balance)
        self._transaction_fee = transaction_fee
        
    def withdraw(self, amount):
        """Override the withdraw method to include transaction fee."""
        total_amount = amount + self._transaction_fee
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False
        if total_amount > self._balance:
            return False
        self._balance -= total_amount
        return True
    
class BusinessAccount(BankAccount):
    """Business account with overdraft limit."""
    
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=500):
        """
        Initialize business account.
        
        Args:
            account_number (str): Account ID
            holder_name (str): Business name
            balance (float): Initial balance
            overdraft_limit (float): Maximum negative balance allowed (default $500)
        """
        super().__init__(account_number, holder_name, balance)
        self._overdraft_limit = overdraft_limit
        
    def withdraw(self, amount):
        """Override the withdraw method to allow overdraft."""
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False
        if self._balance - amount < -self._overdraft_limit:
            return False
        self._balance -= amount
        return True
    
if __name__ == "__main__":
    # Example usage
    account = BankAccount("123456789", "John Doe", 1000.0)
    print(account)
    account.deposit(500)
    print(account)
    account.withdraw(200)
    print(account)
    account.withdraw(2200)
    print(account)
    print(account.get_account_info())
    
    # Create different account types
    savings = SavingsAccount("SAV001", "Alice", 1000, 0.03)
    checking = CheckingAccount("CHK001", "Bob", 500, 2.0)
    business = BusinessAccount("BUS001", "Acme Corp", 1000, 500)

    # Savings account - apply interest
    print("=== Savings Account ===")
    print(savings)
    interest = savings.apply_interest()
    print(f"Interest earned: ${interest}")
    print(savings)

    # Checking account - withdraw with fee
    print("\n=== Checking Account ===")
    print(checking)
    checking.withdraw(50)  # Costs $52 total
    print(checking)

    # Business account - use overdraft
    print("\n=== Business Account ===")
    print(business)
    business.withdraw(1200)  # Goes negative
    print(business)
    print(f"Can withdraw $400 more: {business.withdraw(400)}")  # False, exceeds limit
    print(f"Can withdraw $300 more: {business.withdraw(300)}")  # True, within limit
    print(business)

    # All types inherit basic methods from BankAccount
    print("\n=== All accounts can deposit ===")
    savings.deposit(100)
    checking.deposit(100)
    business.deposit(100)

    print(f"Savings balance: ${savings.get_balance()}")
    print(f"Checking balance: ${checking.get_balance()}")
    print(f"Business balance: ${business.get_balance()}")