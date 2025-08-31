def shift_letters(s, n):
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
            empty_string += letter

    return empty_string


if __name__ == "__main__":
    print(shift_letters("tom-CRUISE", 2))
