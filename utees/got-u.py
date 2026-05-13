import random
import datetime

# Database sederhana menggunakan dictionary dan list
data_buku = {}
data_anggota = {}
riwayat_transaksi = []
transaksi_counter = 1

def get_tanggal_sekarang():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
    
    # MENU 1: Tambah Data Buku
    if pilihan == '1':
        print("\n--- Tambah Data Buku ---")
        while True:
            kode_buku = input("Masukkan Kode Buku: ")
            if kode_buku in data_buku:
                print("Notif: Kode sama! Kode buku sudah ada, silakan masukkan kode lain.")
            else:
                break
        
        judul_buku = input("Judul Buku: ")
        penulis = input("Penulis: ")
        tahun_terbit = input("Tahun Terbit: ")
        
        data_buku[kode_buku] = {
            'judul': judul_buku,
            'penulis': penulis,
            'tahun': tahun_terbit,
            'status': 'Tersedia'
        }
        print("Data buku berhasil ditambahkan!")

    # MENU 2: Tambah Data Anggota
    elif pilihan == '2':
        print("\n--- Tambah Data Anggota ---")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        no_hp = input("No HP: ")
        
        # Output: Nomor anggota random
        no_anggota = "ANG" + str(random.randint(1000, 9999))
        data_anggota[no_anggota] = {
            'nama': nama,
            'alamat': alamat,
            'no_hp': no_hp
        }
        print(f"Data anggota berhasil disimpan. Nomor anggota Anda: {no_anggota}")

    # MENU 3: Pinjam Buku
    elif pilihan == '3':
        print("\n--- Pinjam Buku ---")
        no_anggota = input("Masukkan Nomor Anggota: ")
        
        if no_anggota not in data_anggota:
            print("Nomor anggota tidak ditemukan!")
            continue
            
        anggota = data_anggota[no_anggota]
        # Output 1
        print(f"\nData Anggota -> Nama: {anggota['nama']}, Alamat: {anggota['alamat']}, No HP: {anggota['no_hp']}")
        
        while True:
            kode_buku = input("Masukkan Kode Buku yang akan dipinjam: ")
            if kode_buku not in data_buku:
                print("Notif: Kode tidak tersedia.")
            else:
                buku = data_buku[kode_buku]
                if buku['status'] != 'Tersedia':
                    print(f"Buku '{buku['judul']}' tidak bisa dipinjam (Status: {buku['status']}).")
                    break # Keluar dari loop input buku karena buku tidak tersedia
                else:
                    # Proses peminjaman (Output 2)
                    no_transaksi = f"TRX{transaksi_counter:03d}"
                    transaksi_counter += 1
                    tgl_pinjam = get_tanggal_sekarang()
                    
                    buku['status'] = 'Dipinjam'
                    
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
                    riwayat_transaksi.append(transaksi)
                    
                    print("\n-- Peminjaman Berhasil --")
                    print(f"Nomor Transaksi : {no_transaksi}")
                    print(f"Nama Anggota    : {anggota['nama']}")
                    print(f"Judul Buku      : {buku['judul']}")
                    print(f"Tanggal Pinjam  : {tgl_pinjam}")
                    break

    # MENU 4: Kembalikan Buku
    elif pilihan == '4':
        print("\n--- Kembalikan Buku ---")
        while True:
            kode_buku = input("Masukkan Kode Buku yang dikembalikan: ")
            if kode_buku not in data_buku:
                print("Notif: Kode tidak tersedia.")
            else:
                buku = data_buku[kode_buku]
                if buku['status'] == 'Tersedia':
                    print("Notif: Buku ini tidak sedang dipinjam.")
                    break
                else:
                    # Proses pengembalian (Output 1)
                    tgl_kembali = get_tanggal_sekarang()
                    buku['status'] = 'Tersedia'
                    
                    # Update data di riwayat transaksi
                    for trx in reversed(riwayat_transaksi):
                        if trx['kode_buku'] == kode_buku and trx['status'] == 'Dipinjam':
                            trx['tgl_kembali'] = tgl_kembali
                            trx['status'] = 'Dikembalikan'
                            
                            print("\n-- Pengembalian Berhasil --")
                            print(f"Nomor Transaksi : {trx['no_transaksi']}")
                            print(f"Nama Anggota    : {trx['nama_anggota']}")
                            print(f"Judul Buku      : {trx['judul_buku']}")
                            print(f"Tanggal Kembali : {tgl_kembali}")
                            break
                    break

    # MENU 5: Info Anggota
    elif pilihan == '5':
        print("\n--- Info Anggota ---")
        while True:
            no_anggota = input("Masukkan Nomor Anggota: ")
            if no_anggota not in data_anggota:
                print("Notif: Anggota tidak ditemukan.")
            else:
                break
        
        anggota = data_anggota[no_anggota]
        # Cari buku yang sedang dipinjam oleh anggota ini
        buku_dipinjam = [trx for trx in riwayat_transaksi if trx['no_anggota'] == no_anggota and trx['status'] == 'Dipinjam']
        
        if len(buku_dipinjam) > 0:
            # Output 2 (Jika anggota pinjam ada)
            print(f"\nHeader : Nomor Anggota: {no_anggota}, Nama: {anggota['nama']}, Alamat: {anggota['alamat']}, Nomor HP: {anggota['no_hp']}")
            print("DAFTAR BUKU YANG SEDANG DIPINJAM:")
            print(f"{'No. Urut':<10} | {'Kode Buku':<10} | {'Judul Buku':<25} | {'Status':<15}")
            print("-" * 65)
            for i, trx in enumerate(buku_dipinjam, 1):
                print(f"{i:<10} | {trx['kode_buku']:<10} | {trx['judul_buku']:<25} | {trx['status']:<15}")
        else:
            # Output 2 (Jika anggota belum pinjam)
            print("Notif: Tidak ada buku yang sedang dipinjam.")

    # MENU 6: Daftar Buku
    elif pilihan == '6':
        print("\n--- Daftar Buku ---")
        if not data_buku:
            print("Notif: Belum ada data buku.")
        else:
            print(f"{'No':<5} | {'Kode Buku':<10} | {'Judul Buku':<25} | {'Penulis':<20} | {'Tahun':<6} | {'Status':<15}")
            print("-" * 90)
            no = 1
            for kode, info in data_buku.items():
                print(f"{no:<5} | {kode:<10} | {info['judul']:<25} | {info['penulis']:<20} | {info['tahun']:<6} | {info['status']:<15}")
                no += 1

    # MENU 7: Riwayat Peminjaman
    elif pilihan == '7':
        print("\n--- Riwayat peminjaman ---") # Output Header
        if not riwayat_transaksi:
            print("Belum ada riwayat transaksi.")
        else:
            print(f"{'No':<4} | {'No Transaksi':<13} | {'Tgl Pinjam':<20} | {'Tgl Kembali':<20} | {'Nama Anggota':<15} | {'Kode Buku':<10} | {'Judul':<20} | {'Status'}")
            print("-" * 135)
            for i, trx in enumerate(riwayat_transaksi, 1):
                print(f"{i:<4} | {trx['no_transaksi']:<13} | {trx['tgl_pinjam']:<20} | {trx['tgl_kembali']:<20} | {trx['nama_anggota']:<15} | {trx['kode_buku']:<10} | {trx['judul_buku']:<20} | {trx['status']}")

    # MENU 8: Keluar
    elif pilihan == '8':
        print("Keluar Program... Terima kasih telah menggunakan Sistem Perpustakaan.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-8.")
