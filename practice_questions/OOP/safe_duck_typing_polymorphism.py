class Bird:
    def make_sound(self):
        return "Chirp"


class Dog:
    def make_sound(self):
        return "Woof!"


def play_sound(my_obj, my_obj2):
    """
    This function takes two objects and joins the sounds they make.
    It’s important that both make_sound methods return the same type (strings),
    otherwise trying to join them would cause errors.
    Keeping the return types consistent makes the function work smoothly.
    """
    return my_obj.make_sound() + " " + my_obj2.make_sound()


b1 = Bird()
d1 = Dog()

print("-------")

print(play_sound(b1, d1))
