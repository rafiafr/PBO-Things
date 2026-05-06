import math

def l_persegipjg (pjg, lbr):
    return pjg * lbr

def l_persegi (sisi):
    return sisi * sisi

def l_segitiga (a, t):
    return 0.5 * a * t

def l_lingkaran (jjari):
    return math.pi * jjari ** 2


s = int (input("Masukkan sisi persegi : "))
print("Hasil luas persegi : ", l_persegi (s))
print("\n")

p = int (input("Masukkan panjang persegi panjang: "))
l = int (input("Masukkan luas persegi panjang :"))
print("Hasil luas persegi panjang: ", l_persegipjg (p, l))
print("\n")

alas = int (input("Masukkan alas segitiga : "))
tinggi = int (input("Masukkan tinggi segitiga : "))
print("Hasil luas segitiga: ", l_segitiga (alas, tinggi))
print("\n")

r = int (input("Masukkan jari-jari lingkaran: "))
print("Hasil luas lingkaran: ", l_lingkaran (r))
print("\n")