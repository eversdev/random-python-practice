class SafeBox:
    """
    SafeBox class with one instance attribute and two methods.

    The instance attribute __code is initially set to None.

    The set_code method sets the code based on user input.

    The check_code method checks if the input matches the
    stored code and returns a message.
    """

    def __init__(self):
        """Initialize SafeBox with a private __code attribute set to None."""
        self.__code = None

    def set_code(self) -> str:
        """
        Set the safe box code.

        Prompt the user to enter a 4-digit code.

        Returns:
        str: A message indicating if the code is too long,
        too short, or successfully set.
        """

        while True:
            try:
                user_input = input("Enter a 4-digit code: ")

                if len(user_input) > 4:
                    return "The code you entered exceeds 4 digits."
                elif len(user_input) < 4:
                    return "The code you entered is less than 4 digits."
                else:
                    self.__code = int(user_input)
                    return f"You have entered {user_input} as your code."
            except ValueError:
                return "Invalid input: please enter only numeric digits"

    def check_code(self, user_input) -> str:
        """
        Check if the provided code matches the stored code.

        Parameters:
        user_input (str): The code to check.

        Returns:
        str: A message indicating if the entered code is correct or incorrect.
        """
        if user_input == self.__code:
            return "Code entered correctly."
        else:
            return "Incorrect code entered."


if __name__ == "__main__":
    s1 = SafeBox()
    s1.set_code()

    print(s1.check_code("1234"))

    print()
    print()
    s2 = SafeBox()
    print(s2.__dict__)

    print()
    print()
    s2.__code = "1234"

    print()
    print()
    print(s2.__dict__)
    print(len(s2.__dict__) == 2)




 s3 = SafeBox()
 print(s3.__dict__ = 3 )




