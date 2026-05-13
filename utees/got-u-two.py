import random
import datetime

class SistemPerpustakaan:
    # Method __init__ ini akan pertama kali dipanggil saat objek dibuat.
    # Berfungsi sebagai tempat penyimpanan data (database sementara).
    def __init__(self):
        self.data_buku = {}         # Dictionary untuk menyimpan data buku berdasarkan kode_buku
        self.data_anggota = {}      # Dictionary untuk menyimpan data anggota berdasarkan no_anggota
        self.riwayat_transaksi = [] # List untuk menyimpan riwayat peminjaman/pengembalian
        self.transaksi_counter = 1  # Variabel untuk membuat nomor urut transaksi otomatis

    # Fungsi bantuan (helper) untuk mendapatkan waktu saat ini dari sistem
    def get_tanggal_sekarang(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ==========================================
    # MENU 1: FUNGSI TAMBAH DATA BUKU
    # ==========================================
    def tambah_buku(self):
        print("\n--- Tambah Data Buku ---")
        # Looping untuk memastikan kode buku yang diinput belum ada di database
        while True:
            kode_buku = input("Masukkan Kode Buku: ")
            if kode_buku in self.data_buku:
                print("Notif: Kode sama! Kode buku sudah ada, silakan masukkan kode lain.")
            else:
                break # Keluar dari loop jika kode buku unik
        
        # Meminta input detail buku lainnya
        judul_buku = input("Judul Buku: ")
        penulis = input("Penulis: ")
        tahun_terbit = input("Tahun Terbit: ")
        
        # Menyimpan data buku ke dalam dictionary data_buku
        self.data_buku[kode_buku] = {
            'judul': judul_buku,
            'penulis': penulis,
            'tahun': tahun_terbit,
            'status': 'Tersedia' # Status default saat pertama ditambahkan
        }
        print("Data buku berhasil ditambahkan!")

    # ==========================================
    # MENU 2: FUNGSI TAMBAH DATA ANGGOTA
    # ==========================================
    def tambah_anggota(self):
        print("\n--- Tambah Data Anggota ---")
        # Meminta input data diri anggota
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        no_hp = input("No HP: ")
        
        # Membuat nomor anggota secara acak (random) antara 1000 - 9999
        no_anggota = "ANG" + str(random.randint(1000, 9999))
        
        # Menyimpan data anggota ke dalam dictionary data_anggota
        self.data_anggota[no_anggota] = {
            'nama': nama,
            'alamat': alamat,
            'no_hp': no_hp
        }
        print(f"Data anggota berhasil disimpan. Nomor anggota Anda: {no_anggota}")

    # ==========================================
    # MENU 3: FUNGSI PINJAM BUKU
    # ==========================================
    def pinjam_buku(self):
        print("\n--- Pinjam Buku ---")
        # Input 1: Nomor anggota
        no_anggota = input("Masukkan Nomor Anggota: ")
        
        # Validasi apakah nomor anggota ada di database
        if no_anggota not in self.data_anggota:
            print("Nomor anggota tidak ditemukan!")
            return # Menghentikan proses peminjaman jika anggota tidak ada
            
        # Mengambil data anggota untuk ditampilkan (Output 1)
        anggota = self.data_anggota[no_anggota]
        print(f"\nData Anggota -> Nama: {anggota['nama']}, Alamat: {anggota['alamat']}, No HP: {anggota['no_hp']}")
        
        # Input 2: Kode buku yang ingin dipinjam
        while True:
            kode_buku = input("Masukkan Kode Buku yang akan dipinjam: ")
            
            # Cek apakah kode buku ada di database
            if kode_buku not in self.data_buku:
                print("Notif: Kode tidak tersedia.")
            else:
                buku = self.data_buku[kode_buku]
                # Cek status buku, apakah tersedia atau sedang dipinjam
                if buku['status'] != 'Tersedia':
                    print(f"Buku '{buku['judul']}' tidak bisa dipinjam (Status: {buku['status']}).")
                    break
                else:
                    # Jika buku tersedia, buat transaksi baru dengan prefix TRS
                    no_transaksi = f"TRS{self.transaksi_counter:03d}"
                    self.transaksi_counter += 1
                    tgl_pinjam = self.get_tanggal_sekarang()
                    
                    # Ubah status buku menjadi 'Dipinjam'
                    buku['status'] = 'Dipinjam'
                    
                    # Buat record transaksi
                    transaksi = {
                        'no_transaksi': no_transaksi,
                        'no_anggota': no_anggota,
                        'nama_anggota': anggota['nama'],
                        'kode_buku': kode_buku,
                        'judul_buku': buku['judul'],
                        'tgl_pinjam': tgl_pinjam,
                        'tgl_kembali': '-',
                        'status': 'Dipinjam'
                    }
                    # Masukkan ke dalam list riwayat_transaksi
                    self.riwayat_transaksi.append(transaksi)
                    
                    # Tampilkan bukti peminjaman (Output 2)
                    print("\n-- Peminjaman Berhasil --")
                    print(f"Nomor Transaksi : {no_transaksi}")
                    print(f"Nama Anggota    : {anggota['nama']}")
                    print(f"Judul Buku      : {buku['judul']}")
                    print(f"Tanggal Pinjam  : {tgl_pinjam}")
                    break

    # ==========================================
    # MENU 4: FUNGSI KEMBALIKAN BUKU
    # ==========================================
    def kembalikan_buku(self):
        print("\n--- Kembalikan Buku ---")
        while True:
            kode_buku = input("Masukkan Kode Buku yang dikembalikan: ")
            
            # Cek ketersediaan kode buku
            if kode_buku not in self.data_buku:
                print("Notif: Kode tidak tersedia.")
            else:
                buku = self.data_buku[kode_buku]
                
                # Memastikan buku memang sedang dipinjam
                if buku['status'] == 'Tersedia':
                    print("Notif: Buku ini tidak sedang dipinjam.")
                    break
                else:
                    # Proses pengembalian
                    tgl_kembali = self.get_tanggal_sekarang()
                    
                    # Kembalikan status buku menjadi 'Tersedia'
                    buku['status'] = 'Tersedia'
                    
                    # Cari transaksi terakhir untuk buku ini di riwayat transaksi menggunakan variabel trs
                    for trs in reversed(self.riwayat_transaksi):
                        if trs['kode_buku'] == kode_buku and trs['status'] == 'Dipinjam':
                            trs['tgl_kembali'] = tgl_kembali
                            trs['status'] = 'Dikembalikan'
                            
                            # Tampilkan bukti pengembalian (Output 1)
                            print("\n-- Pengembalian Berhasil --")
                            print(f"Nomor Transaksi : {trs['no_transaksi']}")
                            print(f"Nama Anggota    : {trs['nama_anggota']}")
                            print(f"Judul Buku      : {trs['judul_buku']}")
                            print(f"Tanggal Kembali : {tgl_kembali}")
                            break
                    break

    # ==========================================
    # MENU 5: FUNGSI INFO ANGGOTA
    # ==========================================
    def info_anggota(self):
        print("\n--- Info Anggota ---")
        # Validasi anggota
        while True:
            no_anggota = input("Masukkan Nomor Anggota: ")
            if no_anggota not in self.data_anggota:
                print("Notif: Anggota tidak ditemukan.")
                return # Kembali ke menu utama jika tidak ketemu
            else:
                break
        
        anggota = self.data_anggota[no_anggota]
        
        # Mencari daftar buku yang berstatus 'Dipinjam' oleh anggota ini
        buku_dipinjam = [trs for trs in self.riwayat_transaksi if trs['no_anggota'] == no_anggota and trs['status'] == 'Dipinjam']
        
        # Jika ada buku yang sedang dipinjam
        if len(buku_dipinjam) > 0:
            print(f"\nHeader : Nomor Anggota: {no_anggota}, Nama: {anggota['nama']}, Alamat: {anggota['alamat']}, Nomor HP: {anggota['no_hp']}")
            print("DAFTAR BUKU YANG SEDANG DIPINJAM:")
            print(f"{'No':<5} | {'Kode Buku':<10} | {'Judul Buku':<25} | {'Status':<15}")
            print("-" * 65)
            # Menampilkan list buku
            for i, trs in enumerate(buku_dipinjam, 1):
                print(f"{i:<5} | {trs['kode_buku']:<10} | {trs['judul_buku']:<25} | {trs['status']:<15}")
        else:
            # Jika tidak ada tanggungan pinjaman
            print("Notif: Tidak ada buku yang dipinjam")

    # ==========================================
    # MENU 6: FUNGSI DAFTAR BUKU
    # ==========================================
    def daftar_buku(self):
        print("\n--- Daftar Buku ---")
        # Mengecek apakah dictionary data_buku kosong
        if not self.data_buku:
            print("Notif: Belum ada data buku")
        else:
            # Menampilkan tabel mendatar
            print(f"{'No':<5} | {'Kode Buku':<10} | {'Judul Buku':<25} | {'Penulis':<20} | {'Tahun':<6} | {'Status':<15}")
            print("-" * 90)
            no = 1
            for kode, info in self.data_buku.items():
                print(f"{no:<5} | {kode:<10} | {info['judul']:<25} | {info['penulis']:<20} | {info['tahun']:<6} | {info['status']:<15}")
                no += 1

    # ==========================================
    # MENU 7: FUNGSI RIWAYAT PEMINJAMAN
    # ==========================================
    def tampilkan_riwayat(self):
        print("\nRiwayat peminjaman") # Output Header
        # Mengecek apakah belum ada transaksi yang terjadi
        if not self.riwayat_transaksi:
            print("Belum ada riwayat transaksi.")
        else:
            # Menampilkan tabel mendatar riwayat transaksi secara lengkap (Header diubah jadi No Trs)
            print(f"{'No':<4} | {'No Trs':<10} | {'Tgl Pinjam':<20} | {'Tgl Kembali':<20} | {'Nama Anggota':<15} | {'Kode Buku':<10} | {'Judul':<20} | {'Status'}")
            print("-" * 125)
            for i, trs in enumerate(self.riwayat_transaksi, 1):
                print(f"{i:<4} | {trs['no_transaksi']:<10} | {trs['tgl_pinjam']:<20} | {trs['tgl_kembali']:<20} | {trs['nama_anggota']:<15} | {trs['kode_buku']:<10} | {trs['judul_buku']:<20} | {trs['status']}")

    # ==========================================
    # FUNGSI UTAMA: MENJALANKAN PROGRAM (MENU LOOP)
    # ==========================================
    def jalankan(self):
        # Infinite loop agar menu terus tampil sampai user memilih angka 8
        while True:
            print("\n" + "="*40)
            print("SISTEM PERPUSTAKAAN")
            print("="*40)
            print("1. Tambah Data Buku")
            print("2. Tambah Data Anggota")
            print("3. Pinjam Buku")
            print("4. Kembalikan Buku")
            print("5. Info Anggota")
            print("6. Daftar Buku")
            print("7. Riwayat Peminjaman")
            print("8. Keluar")
            print("="*40)
            
            pilihan = input("Pilih menu (1-8): ")
            
            # Percabangan untuk memanggil method sesuai input user
            if pilihan == '1':
                self.tambah_buku()
            elif pilihan == '2':
                self.tambah_anggota()
            elif pilihan == '3':
                self.pinjam_buku()
            elif pilihan == '4':
                self.kembalikan_buku()
            elif pilihan == '5':
                self.info_anggota()
            elif pilihan == '6':
                self.daftar_buku()
            elif pilihan == '7':
                self.tampilkan_riwayat()
            elif pilihan == '8':
                print("Keluar Program... Terima kasih!")
                break # Menghentikan loop yang berarti program selesai
            else:
                print("Pilihan tidak valid. Silakan pilih menu 1-8.")

# ==========================================
# BLOK EKSEKUSI PROGRAM
# ==========================================
if __name__ == "__main__":
    # 1. Membuat/instansiasi objek dari class SistemPerpustakaan
    aplikasi = SistemPerpustakaan()
    # 2. Menjalankan fungsi utama yang berisi menu
    aplikasi.jalankan()
