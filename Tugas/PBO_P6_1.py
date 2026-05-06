class Mhs:
    institusi = "Institut Teknologi & Bisnis Asia Malang"
    jumlah_mhs = 0

    def __init__(self, nama, nim):
        self._nama = nama
        self._nim = nim
        self._nilai = 0
        Mhs.jumlah_mhs += 1

    # Property
    @property
    def nama(self):
        return self._nama
    @property
    def nim(self):
        return self._nim
    @property
    def nilai(self): # Menampilkan nilai mahasiswa
        return self._nilai
    
    # Property Setter
    @nama.setter
    def nama(self, value):
        self._nama = value
    @nim.setter
    def nim(self, value):
        self._nim = value
    @nilai.setter
    def nilai(self, skor):
        if 0 <= skor <= 100:
            self._nilai = skor
        else:
            print("Nilai harus antara 0 dan 100!")

    @nilai.deleter
    def nilai(self):
        print(f"Menghapus data nilai untuk {self.nama}...")
        self._nilai = 0

    @staticmethod
    def cek_kelulusan(skor):
        return "LULUS" if skor >= 60 else "TIDAK LULUS"
    
    @classmethod
    def ubah_institusi(cls, nama_baru):
        #mengubah nilai atribut class
        cls.institusi = nama_baru
        print(f"Nama institusi diperbarui menjadi: {cls.institusi}")

def banner():
    print("="*70)
    dbannert = f"Nilai Mahasiswa {Mhs.institusi}"
    print(dbannert.center(70))
    print("="*70)
    

# --------------------------------------------------------------------------
banner()
# Obyek mhs1
mhs1 = Mhs("Andi", "12345")
# Merubah nilai mhs1 menggunakan setter
mhs1.nilai = 85
# Menampilkan nama dan nilai mhs1
print (f"Mahasiswa: {mhs1.nama}, Nilai: {mhs1.nilai}")
# Mengecek nilai mhs1 lulus atau tidak
status = Mhs.cek_kelulusan(mhs1.nilai)
print (f"Status: {status}")
# Merubah nama institusi menggunakan class method
Mhs.ubah_institusi("Universitas Asia Malang")
# Menghapus nilai mhs1 menggunakan deleter
del mhs1.nilai
print (f"Nilai setelah dihapus: {mhs1.nilai}")

print("\n") # -------------------------------------------------------------

mhs2 = Mhs("Budi", "67890" )
mhs2.nilai = 55
print(f"Mahasiswa: {mhs2.nama}, Nilai: {mhs2.nilai}")
status = Mhs.cek_kelulusan(mhs2.nilai)
print(f"Status: {status}")
print(f"Institusi Mahasiswa: {mhs2.nama} berasal dari {Mhs.institusi}")

print("\n") # -------------------------------------------------------------

