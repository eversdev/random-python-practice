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
        if isinstance(user_input, int):
                self.__balance = user_input
                print(f"You have set the balance to {user_input}")
        else:
            print("Not an int!")





