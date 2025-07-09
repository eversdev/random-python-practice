class Account:
    """
    Demonstrates private attributes and controlled access via getter and setter methods.
    """
    def __init__(self, name: str, balance: int):
        """
        Initialize an Account instance.
        """
        self.name = name
        self.__balance = balance

    def __str__(self) -> str:
        """
        Return a string representation of the account.
        """
        return f"{self.name} is an object of the Account class."
    
    def get_balance(self) -> int:
        """
        Get the account balance.
        """
        return self.__balance
    
    def set_balance(self, user_input: int) -> None:
        """
        Set the account balance if the input is an int; otherwise, print an error.
        """
        try:
             new_balance = int(user_input)
             self.__balance = new_balance
        except ValueError:
             raise ValueError("Invalid input! Please enter a valid integer.")
        





if __name__ == "__main__":
    a1 = Account("John", 500)
    print(a1.__balance())
    # This block runs only when the script is executed directly.
    # It prevents code from running during imports (e.g., when running tests).
    # Useful for quick manual testing or script execution.



