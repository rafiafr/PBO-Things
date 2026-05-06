class Mhs:
    institusi = "Institut Teknologi dan Bisnis Asia Malang"
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

    # ==========================================
    # MODIFIKASI TANTANGAN DIMULAI DARI SINI
    # ==========================================

    # Tantangan 2: Perhitungan Grade
    @property
    def grade(self):
        if self._nilai < 50:
            return 'E'
        elif self._nilai < 55:
            return 'D'
        elif self._nilai < 65:
            return 'C'
        elif self._nilai < 80:
            return 'B'
        else:
            return 'A'

    # Tantangan 3: Method Menampilkan Tabel Horizontal
    @classmethod
    def tampilkan_tabel(cls, daftar_mhs):
        print(f"\nData seluruh mahasiswa {cls.institusi}")
        print("=========================================================================")
        print(f"{'NIM':<15} {'NAMA':<25} {'NILAI':<10} {'GRADE':<10}")
        print("=========================================================================")
        for mhs in daftar_mhs:
            # Format .1f digunakan agar nilai tampil dengan satu angka desimal (misal: 87.0)
            print(f"{mhs.nim:<15} {mhs.nama:<25} {float(mhs.nilai):<10.1f} {mhs.grade:<10}")
        print("=========================================================================")


# Tantangan 1: Program Utama dengan Perulangan
if __name__ == "__main__":
    daftar_mahasiswa = []
    
    # Inputan berapa Jumlah obyek
    jumlah = int(input("Masukkan jumlah obyek mahasiswa: "))

    # Perulangan input NIM, NAMA, NILAI
    for i in range(jumlah):
        print(f"\nInput data mahasiswa ke-{i+1}")
        nim = input("Masukkan NIM   : ")
        nama = input("Masukkan Nama  : ")
        nilai = float(input("Masukkan Nilai : "))
        
        # Membuat objek baru dan mengisi nilainya
        mhs_baru = Mhs(nama, nim)
        mhs_baru.nilai = nilai
        daftar_mahasiswa.append(mhs_baru)

    # Memanggil method tabel
    Mhs.tampilkan_tabel(daftar_mahasiswa)