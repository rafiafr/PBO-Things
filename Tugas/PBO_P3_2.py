class hero():
    def __init__(self, nama, health, power, armor):
        self.nama = nama
        self.health = health
        self.power = power
        self.armor = armor

hero1 = hero('Superman', 100, 50, 20)
hero2 = hero('Batman', 80, 40, 15)
hero3 = hero('Spiderman', 90, 45, 18)
hero4 = hero('Ironman', 120, 60, 25)
hero5 = hero('Thor', 150, 70, 30)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
print(hero4.__dict__)
print(hero5.__dict__)