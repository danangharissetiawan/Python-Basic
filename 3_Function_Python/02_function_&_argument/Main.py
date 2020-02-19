# function menggunakan argument sederhana
def siswa(nama):
    print('siswa ini bernama:', nama)


siswa('wowok')

print('=' * 68)

# function menggunakan keyword argumemt


def guru(nama, mapel):
    print('guru ini bernama: ', nama)
    print('mengajar: ', mapel)


nama = 'Septi'
mapel = 'Matematika'
guru(nama=nama, mapel=mapel)
print('=' * 68)

# function dengan menggunakan default argument


def penjagaSkolah(nama='-', sift='pagi', sifat='baik'):
    print('Satpam ini bernama: ', nama)
    print('Sift :', sift)
    print('Sifat :', sifat)


penjagaSkolah(nama='Imam', sift='Malam', sifat='Galak')

print('=' * 68)

penjagaSkolah()  # otomatis akan mengambil defaultnya
