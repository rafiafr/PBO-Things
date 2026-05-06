class hero:
    def __init__ (self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    def siapa (self):
        print("Character Name: " + self.name)

    def healthUp(self, up):
        self.health += up

    def getHealth(self):
        return self.health
    
superman = hero ('Himmel', 100, 20, 10)
hero2 = hero ('Frieren', 101, 25, 15)

superman.siapa()
superman.healthUp(10)
print('Health Point: ' + str(superman.getHealth()))