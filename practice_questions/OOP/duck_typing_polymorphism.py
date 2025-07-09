class Bird:
    def make_sound(self):
        return "Chirp"


class Dog:
    def make_sound(self):
        print("Woof!")


def play_sound(my_obj):
    return my_obj.make_sound()


b1 = Bird()
print(play_sound(b1))

print("-------")

d1 = Dog()
play_sound(d1)
