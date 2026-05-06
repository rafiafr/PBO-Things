class Mhs:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

    @property
    def nim(self):
        return self._nim
    
    @property
    def nama(self):
        return self._nama
    
    @nim.setter
    def nim(self, input):
        self._nim = input

    @nama.setter
    def nama(self, input):
        self._nama = input

class Mhs_S1 (Mhs):
    def __init__(self, nim, nama):
        Mhs.__init__(self, nim, nama)
        self.jenjang = "Sarjana"
        self.maxSemester = 14

class Mhs_S2 (Mhs):
    def __init__(self, nim, nama):
        super().__init__(nim, nama)
        self.jenjang = "Pascasarjana"
        self.maxSemester = 8 

mhs_asia1 = Mhs_S1("210001", "Andi")
mhs_asia2 = Mhs_S2("220001", "Budi")

print(f"Nama : {mhs_asia1.nama}, NIM: {mhs_asia1.nim}, Jenjang: {mhs_asia1.jenjang}, Max Semester: {mhs_asia1.maxSemester}")
print(f"Nama : {mhs_asia2.nama}, NIM: {mhs_asia2.nim}, Jenjang: {mhs_asia2.jenjang}, Max Semester: {mhs_asia2.maxSemester}")

mhs_asia1.nim = "210002"
mhs_asia1.nama = "Andi Smith"

print(f"Nama : {mhs_asia1.nama}, NIM: {mhs_asia1.nim}, Jenjang: {mhs_asia1.jenjang}, Max Semester: {mhs_asia1.maxSemester}")
