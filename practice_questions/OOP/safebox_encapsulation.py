class SafeBox:
    """
    SafeBox class with one instance attribute and two methods.

    The instance attribute __code is initially set to None.

    The set_code method sets the code based on user input.

    The check_code method checks if the input matches the stored code and returns a message.
    """
    def __init__(self):
        self.__code = None
        
    def set_code(self, user_input):
        self.__code = user_input
        if len(user_input) > 4:
            return "code you entered is exceeds 4 digits"
        elif len(user_input) < 4:
            return "code you entered is less than 4 digits"
        else:
            return user_input
    
    def check_code(self, user_input):
        if user_input == self.__code:
            return "entered real one"
        else:
            return "entered incorrect code"




