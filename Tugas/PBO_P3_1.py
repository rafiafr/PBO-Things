class mhs():
    nim = "252011184"
    nama = "Rafi"
    gender = "Laki-laki"
    prodi = "Teknik Informatika"

saya=mhs()
print('Nama Saya: '+ saya.nama)
print('Kuliah di Instirur Asia dengan NIM ', saya.nim, ' di prodi', saya.prodi)


print("\n") #-----------------------------------------------

class mhss():
    pass

saya = mhss()
temanku_1 = mhss()
temanku_2 = mhss()

saya.nim = "252011184"
saya.nama = "Raffi"
saya.gender = "Laki"
saya.prodi = "Informatika"

temanku_1.nim = "25211122"
temanku_1.nama = "Verria"
temanku_1.gender = "Perempuan"
temanku_1.prodi = "Tata Boga"

temanku_2.nim = "252021183"
temanku_2.nama = "Budi"
temanku_2.gender = "Laki"
temanku_2.prodi = "Teknik Mesin"

print(saya)
print(saya.__dict__)
print("Nama saya " + saya.nama + " dan Nama Teman saya " + temanku_1.nama + " dan " + temanku_2.nama)

print("\n") #-----------------------------------------------

class mhsss():
    def __init__(self, nim, nama, gender, prodi):
        self.nim = nim
        self.nama = nama
        self.gender = gender
        self.prodi = prodi

saya = mhsss('252011184', 'Rafi', 'Laki-laki', 'Teknik Informatika')
friend1 = mhsss ('25211122', 'Verria', 'Perempuan', 'Tata Boga')
friend2 = mhsss ('252021183', 'Budi', 'Laki-laki', 'Teknik Mesin')
print ('Aku seorang ' + saya.gender + ' bersama: ' + friend1.nama + ' kuliah di asia jurusan ' + saya.prodi + ' punya teman di prodi ' + friend1.prodi + ' namanya : ' + friend1.nama)
print('aku juga punya teman ' + friend2.gender + ' di prodi ' + friend2.prodi + ' namanya ' + friend2.nama)
print('NIM kami bertiga adalah :' + saya.nim + ', ' + friend1.nim + ', ' + friend2.nim)