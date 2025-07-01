## SafeBox Class
What it is
SafeBox is a simple little class I made to store a secret 4-digit code. When you create it, you don’t need to give it a code right away — it starts empty (None). You can set the code later and check if someone enters the right one.

How to use it
When you make a SafeBox, no code needed at first.

Use set_code(user_input) to set your 4-digit code. It checks if your code is exactly 4 digits and tells you if it’s too short or too long.

Use check_code(user_input) to check if the code you enter matches the one saved inside.

Example
sf1 = SafeBox()  # No need to give a code when creating it
print(sf1.set_code("1234"))  # Sets the code, returns '1234'
print(sf1.set_code("123"))   # Returns 'code you entered is less than 4 digits'
print(sf1.check_code("1234"))  # Returns 'entered real one'
print(sf1.check_code("0000"))  # Returns 'entered incorrect code'
What you get back
Both the set_code and check_code methods return messages as strings to let you know what happened



## Encapsulation Class

What it is
This class demonstrates how protected instance attributes can be accessed and modified from outside the class, and why this is generally discouraged. It’s not generally encouraged because it breaks encapsulation and can cause unexpected bugs.

How to use it
Create a Book object by passing the title and page number. The _pages attribute is protected but can still be changed directly from outside the class, which is not recommended.

Example
```python
b1 = Book("LOTR", 200)

b1._pages = 250
print(b1.get_pages())  # Now prints 250 instead of 200, the original value
```


## BankAccount Class

What it is  
This class demonstrates how to manage private instance attributes and the difference between accessing them via methods inside the class versus trying to access or modify them from outside the class, including how Python’s name mangling works.

How to use it  
Create an instance of the BankAccount class. Access the private attribute via the getter method (the recommended way). If you try to access or change the private attribute directly from outside, it won’t raise an error but will create a new attribute due to name mangling, which can cause unexpected behavior.

Example

```python
account1 = BankAccount("John", 500)

print(account1)

# Python creates a new __balance attribute on account1 without changing the original private one. It doesn’t actually modify the mangled attribute.
account1.__balance = 400

# Print the real attribute using a method inside the class
print(account1.get_balance())

# Real attribute accessed via name mangling
print(account1._BankAccount__balance)
```


## Overview

This `Account` class was created for demonstration purposes to show how private attributes can be accessed from outside versus inside the class, highlighting the differences and encapsulation.

## Usage

Create an instance of the `Account` class and try to access the private balance attribute using the getter method. You can also change the balance using the setter method, which validates input to maintain data integrity.

If you try to access or modify the private attribute directly from outside the class, it may cause unexpected bugs, errors, or won't behave as intended due to encapsulation and name mangling.

## Important

The setter method only accepts integer values. If invalid input is provided, it will reject it and leave the balance unchanged to avoid accidental data corruption.

## Example

```python
ac1 = Account("John Doe", 500)
print(ac1.get_balance())   # Outputs: 500
ac1.set_balance(1000)      # Sets balance to 1000
ac1.set_balance("abc")     # Prints error and balance remains 1000
'''

