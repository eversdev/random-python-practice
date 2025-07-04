class Bird:
    def make_sound(self):
        return "Chirp"

class Dog:
    def make_sound(self):
        return "Woof!"




def play_sound(my_obj, my_obj2):
    return my_obj.make_sound() + my_obj2.make_sound()




b1 = Bird()
d1 = Dog()

print("-------")

print(play_sound(b1, d1))





