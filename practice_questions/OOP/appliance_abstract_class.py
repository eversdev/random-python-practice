from abc import ABC, abstractmethod

class Appliance(ABC):
    """
    Abstract base class representing a generic appliance.
    Defines an abstract method run() and a concrete method power_status().
    """
    @abstractmethod
    def run(self):
        """
        Abstract method to run the appliance.
        Must be implemented by subclasses.
        """
        pass

    def power_status(self) -> None:
        """
        Concrete method to indicate the appliance is powered on.
        """
        print("Powered On")
    

class Toaster(Appliance):
    """
    Subclass representing a Toaster appliance.
    Implements the abstract run() method.
    """
    def run(self) -> None:
        """
        Runs the toaster by printing a message.
        """
        print("Turn on!")


t1 = Toaster()

t1.run()
t1.power_status()




