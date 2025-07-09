class BankAccount:
    """ ""
    Demonstrates accessing private instance attributes from outside the class
    versus accessing them from within using a getter method.
    """

    def __init__(self, name, balance):
        """
        Initialize a BankAccount object with a public name
        and a private balance attribute.
        """
        self.name = name
        self.__balance = balance

    def __str__(self):
        """
        Return a custom string representation of the BankAccount object.
        """
        return f"This is object {self.name} an object of BankAccount "

    def get_balance(self):
        """
        Getter method to access the private balance attribute.
        """
        return self.__balance

    def set_balance(self):
        """
        placeholder setter method included out of habit but not required for this task
        """
        pass


account1 = BankAccount("John", 500)

print(account1)


# Python creates a new __balance attribute on account1 without changing
# the original private one.
# It doesn’t actually modify the mangled attribute.
account1.__balance = 400

# Print the real atribute using a method inside the class
print(account1.get_balance())

# Real attribute accessed via Name Mangling
print(account1._BankAccount__balance)
