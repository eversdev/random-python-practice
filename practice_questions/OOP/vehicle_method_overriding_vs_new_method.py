class Vehicle:
    """
    Base class representing a generic vehicle.
    """
    def move(self):
        print("Vehicle Moves")



class Car(Vehicle):
    """
    Subclass representing a car.
    """
    def move(self):
        print("Car drives")

    def stop(self):
        print("Vehicle stops!")


class Boat(Vehicle):
    """
    Subclass representing a boat.
    """
    def move(self):
        print("Boat sails")

   

    


def start_engine(my_obj):
    """
    Calls the move method of the passed-in object.

    This shows polymorphism: different objects respond to the same method call.
    """
    my_obj.move()

c1 = Car()
b1 = Boat()

try:
    b1.stop()
except AttributeError:
    print(".stop() method is not a method found in instance of class Boat")
