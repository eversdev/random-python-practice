class Player:
    """
    A simple class representing a player with health management.

    Provides methods to heal and apply damage, while enforcing limits
    (e.g., health cannot exceed 100 or fall below 0).
    """

    def __init__(self):
        """Initializes the player with 0 health."""
        self.__health = 0

    def __str__(self) -> str:
        """
        Returns a custom string representation of the Player object.
        """
        return "Player Object"

    def damage_points(self) -> int:
        """
        Prompts the user to enter damage points and applies it to the player's health.

           - If input is greater than 100, prompts again.
           - If health is already 0, notifies that the opponent has fainted.
           - If valid, subtracts from health and prints the result.
           - Health cannot go below 0.

           Returns:
           int: The player's current health.
        """
        while True:
            dp = int(input("Hit your opponent: "))
            if dp > 100:
                print(f"Invalid damage input: {dp}")
                print("Damage input above 100 please enter numbers 100 or below.")
                continue  # Ask again immediately
            if self.__health == 0:
                print("Opponent's health already at 0 please fill up HP.")
                return self.__health
            self.__health -= dp
            if self.__health > 0:
                print(f"You dealt {dp} damage. Opponents health is now {self.__health}")
                return self.__health
            else:
                self.__health = 0
                print(f"You dealt {dp} damage. Opponents health is now {self.__health}")
                print("Opponent has fainted")
                return self.__health

    def health_points(self) -> int:
        """
        Prompts the user to enter health points and heals the player accordingly.

        - Rejects input ≤ 0 and > 100.
        - Caps health at 100.
        - Prints the new health status.

        Returns:
            int: The player's current health.
        """
        while True:
            try:
                hp = int(input("Enter health points: "))

                if hp <= 0:
                    print("No change in health points are you sure?")
                    continue
                elif hp > 100:
                    print("Healing maxed out!")
                    continue

                self.__health += hp
                if self.__health > 100:
                    self.__health = 100
                    return self.__health
                elif self.__health > 0:
                    print(f"Your hp is now {self.__health}")
                    return self.__health
            except ValueError:
                print("Enter a valid number")


if __name__ == "__main__":
    p1 = Player()

    print(f"{p1} Player health is {p1._Player__health}")

    p1.health_points()

    print(p1._Player__health)

    """
    p1 = Player()
    print(f"{p1} Player health is {p1._Player__health}")
    p1.health_points()
    p1.damage_points()
    print(p1._Player__health)
    """
