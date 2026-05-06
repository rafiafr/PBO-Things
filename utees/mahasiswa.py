class Mahasiswa:
    def __init__(self, nim, nama, prodi, semester):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.semester = semester
        self.daftar_krs = []

    def tambah_krs(self, item_krs):
        self.daftar_krs.append(item_krs)

    def hitung_total_sks_pengajuan(self):
        total = 0
        for item in self.daftar_krs:
            total += item.mata_kuliah.sks
        return total

    def hitung_total_sks_disetujui(self):
        total = 0
        for item in self.daftar_krs:
            if item.status == "DISETUJUI":
                total += item.mata_kuliah.sks
        return total


class MataKuliah:
    def __init__(self, kode_mk, nama_mk, sks, semester):
        self.kode_mk = kode_mk
        self.nama_mk = nama_mk
        self.sks = sks
        self.semester = semester


class ItemKRS:
    def __init__(self, mata_kuliah, status):
        self.mata_kuliah = mata_kuliah
        self.status = status


class SistemKRS:
    def __init__(self):
        self.data_mahasiswa = {}
        self.data_mata_kuliah = {}

    def input_angka(self, pesan):
        while True:
            try:
                nilai = int(input(pesan))
                if nilai <= 0:
                    print("Input harus lebih dari 0.")
                else:
                    return nilai
            except ValueError:
                print("Input harus berupa angka.")

    def cari_mahasiswa(self, nim):
        return self.data_mahasiswa.get(nim)

    def cari_mata_kuliah(self, kode_mk):
        return self.data_mata_kuliah.get(kode_mk)

    def tambah_mahasiswa(self):
        print("\n=== TAMBAHKAN MAHASISWA ===")

        nim = input("Masukkan NIM      : ")

        if nim in self.data_mahasiswa:
            print("NIM sudah terdaftar.")
            return

        nama = input("Masukkan Nama     : ")
        prodi = input("Masukkan Prodi    : ")
        semester = self.input_angka("Masukkan Semester : ")

        mahasiswa = Mahasiswa(nim, nama, prodi, semester)
        self.data_mahasiswa[nim] = mahasiswa

        print("\nData mahasiswa berhasil ditambahkan.")
        print(f"NIM      : {nim}")
        print(f"Nama     : {nama}")
        print(f"Prodi    : {prodi}")
        print(f"Semester : {semester}")

    def tambah_mata_kuliah(self):
        print("\n=== TAMBAHKAN MATA KULIAH ===")

        kode_mk = input("Masukkan Kode MK  : ").upper()

        if kode_mk in self.data_mata_kuliah:
            print("Kode mata kuliah sudah terdaftar.")
            return

        nama_mk = input("Masukkan Nama MK  : ")
        sks = self.input_angka("Masukkan SKS      : ")
        semester = self.input_angka("Masukkan Semester : ")

        mata_kuliah = MataKuliah(kode_mk, nama_mk, sks, semester)
        self.data_mata_kuliah[kode_mk] = mata_kuliah

        print("\nData mata kuliah berhasil ditambahkan.")
        print(f"Kode MK  : {kode_mk}")
        print(f"Nama MK  : {nama_mk}")
        print(f"SKS      : {sks}")
        print(f"Semester : {semester}")

    def ajukan_krs(self):
        print("\n=== AJUKAN KRS ===")

        if len(self.data_mahasiswa) == 0:
            print("Belum ada data mahasiswa.")
            return

        if len(self.data_mata_kuliah) == 0:
            print("Belum ada data mata kuliah.")
            return

        nim = input("Masukkan NIM Mahasiswa: ")
        mahasiswa = self.cari_mahasiswa(nim)

        if mahasiswa is None:
            print("NIM mahasiswa tidak ditemukan.")
            return

        print("\nData Mahasiswa")
        print(f"NIM      : {mahasiswa.nim}")
        print(f"Nama     : {mahasiswa.nama}")
        print(f"Prodi    : {mahasiswa.prodi}")
        print(f"Semester : {mahasiswa.semester}")

        total_sks = mahasiswa.hitung_total_sks_pengajuan()

        if total_sks >= 21:
            print("\nTotal SKS pengajuan sudah mencapai atau melebihi 21 SKS.")
            print("Mahasiswa tidak dapat menambahkan mata kuliah lagi.")
            return

        print("\nSilakan masukkan kode mata kuliah satu per satu.")
        print("Input akan berhenti jika total SKS mencapai atau melebihi 21 SKS.")
        print("Ketik SELESAI jika ingin berhenti sebelum 21 SKS.")

        while total_sks < 21:
            kode_mk = input("\nMasukkan Kode MK: ").upper()

            if kode_mk == "SELESAI":
                print("Input pengajuan KRS dihentikan.")
                break

            mata_kuliah = self.cari_mata_kuliah(kode_mk)

            if mata_kuliah is None:
                print("Kode mata kuliah tidak ditemukan.")
                continue

            sudah_diajukan = False

            for item in mahasiswa.daftar_krs:
                if item.mata_kuliah.kode_mk == kode_mk:
                    sudah_diajukan = True
                    break

            if sudah_diajukan:
                print("Mata kuliah ini sudah pernah diajukan.")
                continue

            if mata_kuliah.semester == mahasiswa.semester:
                status = "DISETUJUI"
            else:
                status = "DITOLAK"

            item_krs = ItemKRS(mata_kuliah, status)
            mahasiswa.tambah_krs(item_krs)

            total_sks += mata_kuliah.sks

            print("\nMata kuliah berhasil diajukan.")
            print(f"Kode MK      : {mata_kuliah.kode_mk}")
            print(f"Nama MK      : {mata_kuliah.nama_mk}")
            print(f"SKS          : {mata_kuliah.sks}")
            print(f"Semester MK  : {mata_kuliah.semester}")
            print(f"Semester Mhs : {mahasiswa.semester}")
            print(f"Status       : {status}")
            print(f"Total SKS    : {total_sks}")

        if total_sks >= 21:
            print("\nPengajuan KRS selesai karena total SKS sudah mencapai atau melebihi 21 SKS.")

    def tampilkan_daftar_mata_kuliah(self):
        print("\n=== DAFTAR MATA KULIAH ===")

        print("-" * 85)
        print(f"{'Kode MK':<15} {'Nama MK':<40} {'SKS':<10} {'Semester':<10}")
        print("-" * 85)

        if len(self.data_mata_kuliah) == 0:
            print("Belum ada data mata kuliah.")
        else:
            for mk in self.data_mata_kuliah.values():
                print(
                    f"{mk.kode_mk:<15} "
                    f"{mk.nama_mk:<40} "
                    f"{mk.sks:<10} "
                    f"{mk.semester:<10}"
                )

        print("-" * 85)

    def info_krs_disetujui(self):
        print("\n=== INFO KRS YANG DISETUJUI ===")

        if len(self.data_mahasiswa) == 0:
            print("Belum ada data mahasiswa.")
            return

        nim = input("Masukkan NIM Mahasiswa: ")
        mahasiswa = self.cari_mahasiswa(nim)

        if mahasiswa is None:
            print("NIM mahasiswa tidak ditemukan.")
            return

        print("\nData Mahasiswa")
        print(f"NIM      : {mahasiswa.nim}")
        print(f"Nama     : {mahasiswa.nama}")
        print(f"Prodi    : {mahasiswa.prodi}")
        print(f"Semester : {mahasiswa.semester}")

        print("\nDaftar Pengajuan KRS")
        print("-" * 120)
        print(
            f"{'No':<5} "
            f"{'Kode MK':<12} "
            f"{'Nama MK':<40} "
            f"{'SKS':<8} "
            f"{'Semester MK':<15} "
            f"{'Semester Mhs':<15} "
            f"{'Status':<15}"
        )
        print("-" * 120)

        if len(mahasiswa.daftar_krs) == 0:
            print("Mahasiswa belum mengajukan KRS.")
        else:
            for nomor, item in enumerate(mahasiswa.daftar_krs, start=1):
                mk = item.mata_kuliah

                print(
                    f"{nomor:<5} "
                    f"{mk.kode_mk:<12} "
                    f"{mk.nama_mk:<40} "
                    f"{mk.sks:<8} "
                    f"{mk.semester:<15} "
                    f"{mahasiswa.semester:<15} "
                    f"{item.status:<15}"
                )

            print("-" * 120)
            print(f"Total SKS Pengajuan : {mahasiswa.hitung_total_sks_pengajuan()} SKS")
            print(f"Total SKS Disetujui : {mahasiswa.hitung_total_sks_disetujui()} SKS")

    def tampilkan_menu(self):
        print("\n====================================")
        print("        SISTEM PENGAJUAN KRS")
        print("====================================")
        print("1. Tambahkan Mahasiswa")
        print("2. Tambahkan Mata Kuliah")
        print("3. Ajukan KRS")
        print("4. Daftar Mata Kuliah")
        print("5. Info KRS yang Disetujui")
        print("6. Keluar")

    def jalankan(self):
        while True:
            self.tampilkan_menu()
            pilihan = input("Pilih menu [1-6]: ")

            if pilihan == "1":
                self.tambah_mahasiswa()
            elif pilihan == "2":
                self.tambah_mata_kuliah()
            elif pilihan == "3":
                self.ajukan_krs()
            elif pilihan == "4":
                self.tampilkan_daftar_mata_kuliah()
            elif pilihan == "5":
                self.info_krs_disetujui()
            elif pilihan == "6":
                print("Program selesai. Terima kasih.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu 1 sampai 6.")


program = SistemKRS()
program.jalankan()