from rumus import l_lingkaran, l_persegipjg, l_persegi, l_segitiga

# ----------------------------------------------------------

def show_menu():
    print ("\n")
    print ("--- Pilih menu Hitung Bangun datar ---")
    print ("1 = Luas Persegi")
    print ("2 = Luas Persegi Panjang")
    print ("3 = Luas Segitiga")
    print ("4 = Luas Lingkaran")
    print ("5 = Luas Exit")
    print ("--------------------------------------")

    menu = int(input("PILIH MENU: "))
    print(" ")

    if menu == 1:
        s = int (input("Masukkan sisi persegi : "))
        print("Hasil luas persegi : ", l_persegi (s))
        print("\n")
        
    elif menu == 2:
        p = int (input("Masukkan panjang persegi panjang: "))
        l = int (input("Masukkan luas persegi panjang :"))
        print("Hasil luas persegi panjang: ", l_persegipjg (p, l))
        print("\n")

    elif menu == 3:
        alas = int (input("Masukkan alas segitiga : "))
        tinggi = int (input("Masukkan tinggi segitiga : "))
        print("Hasil luas segitiga: ", l_segitiga (alas, tinggi))
        print("\n")

    elif menu == 4:
        r = int (input("Masukkan jari-jari lingkaran: "))
        print("Hasil luas lingkaran: ", l_lingkaran (r))
        print("\n")

    elif menu == 5:
        exit()
        
    else:
        print("Tidak ada pada menu!")
        
        
if __name__ == "__main__":
    while(True):
        show_menu()