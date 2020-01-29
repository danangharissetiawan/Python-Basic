# Scope variabel global
# Scope asal variable adalah local, artinya variabel diluar function berbeda dengan variable yang berada didalam function
# sedangkan scope variabel global mencakup didalam dan diluar function

nama = 'Haris'
namaLengkapSaya = 'Danang Haris'


def ubahNama(namaBaru):
    global nama
    namaAsli = 'nama asli saya adalah ' + nama
    nama = 'Sekarang nama saya menjadi ' + namaBaru
    print(namaAsli, 'dan', nama)


ubahNama('Danang')


def namaLengkap(namaLengkap, namaBaru):
    global nama, namaLengkapSaya
    nama = namaBaru
    namaLengkapAsal = 'Nama legkap saya adalah'+namaLengkapSaya + '\n'
    namaLengkapSaya = namaLengkap
    namaLengkapBaru = 'Sekarang nama lengkap saya adalah '+namaLengkapSaya + '\n'
    print(namaLengkapAsal, 'dan', namaLengkapBaru,
          'dan nama baru saya adalah', nama)


namaLengkap('Danang Haris Setiawan', 'Setiawan')
