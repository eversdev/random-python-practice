SafeBox Class
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
