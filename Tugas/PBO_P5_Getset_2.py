class Mhs:
    __jumlah = 0; #private class variable
    def __init__(self, nama, umur):
        self.__nama = nama
        self.__umur = umur
        Mhs.__jumlah += 1

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
    
    # Getter untuk jumlah mahasiswa, tambahan -------------------------

    def getJumlah(self):
        return Mhs.__jumlah
    
    def getJumlah2():
        return Mhs.__jumlah
    
    def getJumlah(self):
        return Mhs.__jumlah
    
    @staticmethod
    def getJumlah3():
        return Mhs.__jumlah
    

mhs_asia = Mhs("Andi", 20)

print(Mhs.get_nama(mhs_asia))
# print(mhs_asia.getJumlah2())
print(Mhs.getJumlah2())

print("============= daerah static method")

print(mhs_asia.getJumlah3())
print(Mhs.getJumlah3())