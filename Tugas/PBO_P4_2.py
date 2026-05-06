class Hero:
    jumlah_Hero = 0

    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        Hero.jumlah_Hero += 1

superman = Hero ('Superman', 100, 20, 10)
print('========== Memanggil Variabel Juumlah ==========')
print('Punya Objek: ' + str(superman.jumlah_Hero)) 
print('Punya class: ' + str(Hero.jumlah_Hero))
print('===== Nilai jumlah hero di object di rubah =====')
superman.jumlah_Hero = 10
print('Punya Objek: ' + str(superman.jumlah_Hero))
print('Punya class: ' + str(Hero.jumlah_Hero))
print('===== Nilai jumlah hero di class di rubah =====')
Hero.jumlah_Hero = 20
print('Punya Objek: ' + str(superman.jumlah_Hero))
print('Punya class: ' + str(Hero.jumlah_Hero))