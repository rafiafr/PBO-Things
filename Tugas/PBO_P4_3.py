class Hero:
    jumlah_hero = 0

    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        Hero.jumlah_hero += 1
        self.__age = 25
        self._weight = 110

spiderman = Hero ('Spiderman', 90, 45, 18)

spiderman.__age = 30
print(spiderman.__dict__)
spiderman._weight = 70
print(spiderman.__dict__)