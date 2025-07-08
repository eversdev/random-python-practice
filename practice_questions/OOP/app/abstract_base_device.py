from abc import ABC, abstractmethod

class Device(ABC):
    """"
    An abstract base class that defines a generic device interface.
    Requires subclasses to implement the start() method.
    """
    @abstractmethod
    def start(self):
        """
        Abstract method meant to be overridden by subclasses.
        Should define how the device starts.
        """
        pass


class Phone(Device):
    """
    Starts the phone by simulating dialing a number.
    """
    def start(self) -> str:
        print("Dial a number")



class Laptop(Device):
    """
    Starts the laptop by simulating powering on.
    """
    def start(self) -> str:
        print("Power on!")



p1 = Phone()
p1.start()

try:
    d1 = Device()
except TypeError as e:
    print("Unable to instantiate abstract class", e)

l1 = Laptop()
l1.start()


def boot_device(device):
    """
    Takes any object with a start() method and calls it.
    Demonstrates abstraction and polymorphism by allowing different device types to be booted the same way.
    """
    device.start()

print("------")
boot_device(p1)
boot_device(l1)