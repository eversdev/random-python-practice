from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def run(self):
        pass

    def power_status(self):
        print("Powered On")
    

class Toaster(Appliance):
    def run(self):
        print("Turn on!")


t1 = Toaster()

t1.run()
t1.power_status()




