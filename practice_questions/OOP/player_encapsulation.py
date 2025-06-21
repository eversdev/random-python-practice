class Player:
    def __init__(self):
        self.__health = 0


    def __str__(self):
        return "Player Object"    

    def damage_points(self):
        dp = int(input("Hit your opponent: "))
        self.__health-=dp
        if self.__health > 0:
            return self.__health
        elif self.__health <= 0:
            self.__health = 0
        

        
    #setter method, should set the health of the player obj without name mangling, cant be above 100 
    #cant be below 0 either
    def health_points(self):
        hp = int(input("Enter health points: "))
        self.__health+=hp                       #idk if u could add none to 100, maybe change to empty str or 0 as default
        if self.__health > 100:
            self.__health = 100
            return self.__health
        elif self.__health <= 100:
            return self.__health
        #return self.__health

        
    

p1 = Player()


print(f"{p1} Player health is {p1._Player__health}")


p1.health_points()
p1.damage_points()

print(p1._Player__health)