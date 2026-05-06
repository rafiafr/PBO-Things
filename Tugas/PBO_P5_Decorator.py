class Mhs:
    def __init__(self, nama, nim):
        self._nama = nama
        self._nim = nim

    @property
    def nama(self):
        return self._nama
    
    @nama.setter
    def nama(self,  value):
        if not value:
            raise ValueError("Nama tidak boleh kososng!")
        self._nama = value

    @property
    def nim(self):
        return self._nim
    
    @nim.setter
    def nim(self, value):
        self._nim = value

mhs_asia = Mhs("Andi", "12345")
print(mhs_asia.nama)
print(mhs_asia.nim)

mhs_asia.nama = "Budi"
mhs_asia.nim = "67890"
print(mhs_asia.nama)
print(mhs_asia.nim)