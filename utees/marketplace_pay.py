import random
from datetime import datetime


# CLASS 1: Generator ID
class GeneratorID:
    @staticmethod
    def generate(existing_ids):
        while True:
            id_data = str(random.randint(10000, 99999))
            if id_data not in existing_ids:
                return id_data


# CLASS 2: Transaksi
class Transaksi:
    def __init__(self, keterangan, debet, kredit, saldo):
        self.tanggal = datetime.now()
        self.keterangan = keterangan
        self.debet = debet
        self.kredit = kredit
        self.saldo = saldo


# CLASS 3: Pengguna
class Pengguna:
    def __init__(self, id_data, nama, id_personal, alamat, kontak_verifikasi, saldo):
        self.id_data = id_data
        self.nama = nama
        self.id_personal = id_personal
        self.alamat = alamat
        self.kontak_verifikasi = kontak_verifikasi
        self.saldo = saldo
        self.riwayat = []

    def tambah_transaksi(self, transaksi):
        self.riwayat.append(transaksi)


# CLASS 4: Sistem
class SistemData:
    def __init__(self):
        self.data_store = {}

    def input_angka(self, pesan):
        while True:
            try:
                nilai = int(input(pesan))
                if nilai < 0:
                    print("Input tidak boleh negatif.")
                else:
                    return nilai
            except ValueError:
                print("Input harus berupa angka.")

    def cari_data(self, id_data):
        return self.data_store.get(id_data)

    # MENU 1
    def tambah_data(self):
        print("\n=== Tambah Data Nasabah ===")

        nama = input("Nama: ")
        id_personal = input("ID Personal: ")
        alamat = input("Alamat: ")
        kontak_verifikasi = input("Kontak Verifikasi: ")
        saldo = self.input_angka("Saldo Awal: ")

        id_data = GeneratorID.generate(self.data_store.keys())

        pengguna = Pengguna(id_data, nama, id_personal, alamat, kontak_verifikasi, saldo)
        self.data_store[id_data] = pengguna

        print(f"Nomor Rekening Anda: {id_data}")

    # MENU 2
    def proses_masuk(self):
        print("\n=== Setor Tunai ===")
        id_data = input("Masukkan No Rekening: ")

        pengguna = self.cari_data(id_data)

        if pengguna:
            jumlah = self.input_angka("Jumlah setor: ")
            pengguna.saldo += jumlah

            trx = Transaksi("Setor Tunai", 0, jumlah, pengguna.saldo)
            pengguna.tambah_transaksi(trx)

            print("Nama:", pengguna.nama)
            print("Saldo akhir:", pengguna.saldo)
        else:
            print("Rekening tidak ditemukan!")

    # MENU 3
    def proses_keluar(self):
        print("\n=== Tarik Tunai ===")
        id_data = input("Masukkan No Rekening: ")

        pengguna = self.cari_data(id_data)

        if pengguna:
            while True:
                jumlah = self.input_angka("Jumlah tarik: ")
                if jumlah > pengguna.saldo:
                    print("Saldo tidak cukup! Input ulang.")
                else:
                    pengguna.saldo -= jumlah

                    trx = Transaksi("Tarik Tunai", jumlah, 0, pengguna.saldo)
                    pengguna.tambah_transaksi(trx)

                    print("Saldo akhir:", pengguna.saldo)
                    break
        else:
            print("Rekening tidak ditemukan!")

    # MENU 4
    def proses_pindah(self):
        print("\n=== Transfer ===")
        id_data = input("Rekening Pengirim: ")

        pengguna = self.cari_data(id_data)

        if pengguna:
            bank = input("Bank tujuan: ")
            norek_tujuan = input("No Rek tujuan: ")
            nama_tujuan = input("Nama tujuan: ")

            while True:
                jumlah = self.input_angka("Jumlah transfer: ")
                if jumlah > pengguna.saldo:
                    print("Saldo tidak cukup! Input ulang.")
                else:
                    pengguna.saldo -= jumlah

                    trx = Transaksi(
                        f"Transfer ke {nama_tujuan} ({bank})",
                        jumlah,
                        0,
                        pengguna.saldo
                    )
                    pengguna.tambah_transaksi(trx)

                    print("Transfer berhasil!")
                    print("Saldo akhir:", pengguna.saldo)
                    break
        else:
            print("Rekening tidak ditemukan!")

    # MENU 5
    def tampil_data(self):
        print("\n=== Info Rekening ===")
        id_data = input("Masukkan No Rekening: ")

        pengguna = self.cari_data(id_data)

        if pengguna:
            print("\n--- DATA NASABAH ---")
            print("Nama:", pengguna.nama)
            print("Alamat:", pengguna.alamat)

            print("\n--- RIWAYAT TRANSAKSI ---")
            print("No | Tanggal | Keterangan | Debet | Kredit | Saldo")

            for i, trx in enumerate(pengguna.riwayat, 1):
                print(f"{i} | {trx.tanggal.strftime('%Y-%m-%d %H:%M:%S')} | "
                      f"{trx.keterangan} | {trx.debet} | {trx.kredit} | {trx.saldo}")
        else:
            print("Rekening tidak ditemukan!")

    def tampilkan_menu(self):
        print("\n=== MENU BANK ===")
        print("1. Tambah Data Nasabah")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Transfer")
        print("5. Info Rekening")
        print("6. Keluar")

    def jalankan(self):
        while True:
            self.tampilkan_menu()
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.tambah_data()
            elif pilihan == "2":
                self.proses_masuk()
            elif pilihan == "3":
                self.proses_keluar()
            elif pilihan == "4":
                self.proses_pindah()
            elif pilihan == "5":
                self.tampil_data()
            elif pilihan == "6":
                print("Keluar program.")
                break
            else:
                print("Pilihan tidak valid!")


# RUN
program = SistemData()
program.jalankan()