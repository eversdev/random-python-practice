def shift_letters(s, n):
    """
    This function takes a string and a number and shifts all the letters in the string
    by that number. Uppercase letters stay uppercase and lowercase stay lowercase.
    Other characters like punctuation or spaces are not changed.

    Args:
    s (str): The string that you want to shift.
    n (int): The number of positions to shift each letter.

    Returns:
    str: A new string with all the letters shifted.
    """
    empty_string = ""
    for letter in s:
        l_position = ord(letter) - ord("a")
        u_position = ord(letter) - ord("A")

        if letter.isalpha():
            if letter.isupper():
                new_position = (u_position + n) % 26
                new_ascii = new_position + ord("A")
                shifted_letter = chr(new_ascii)
                empty_string += shifted_letter
            elif letter.islower():
                new_position = (l_position + n) % 26
                new_ascii = new_position + ord("a")
                shifted_letter = chr(new_ascii)
                empty_string += shifted_letter
        else:
            # Keep non-alphabetic characters unchanged
            # (punctuation, numbers, spaces, etc.)
            empty_string += letter

    return empty_string


if __name__ == "__main__":
    print(shift_letters("tom-CRUISE", 2))
    print("Shifted result:", shift_letters("hello-world", 5))
