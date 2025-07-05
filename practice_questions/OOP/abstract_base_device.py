from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def start(self):
        pass


class Phone(Device):
    def start(self):
        print("Dial a number")



p1 = Phone()

p1.start()