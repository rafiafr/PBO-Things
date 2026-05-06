class Mhs:
    def __init__(self, nama, umur):
        self.__nama = nama
        self.__umur = umur

    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama_baru):
        self.__nama = nama_baru
        
    def get_umur(self):
        return self.__umur
    
    def set_umur(self, umur_baru):
        if umur_baru > 0:
            self.__umur = umur_baru
        else:
            print("Umur harus positif!")

mhs_asia = Mhs("Andi", 20)

print(mhs_asia.get_nama())
print(mhs_asia.get_umur())

mhs_asia.set_nama("Budi")
mhs_asia.set_umur(22)

print(mhs_asia.get_nama())
print(mhs_asia.get_umur())
