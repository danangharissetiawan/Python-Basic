# mendefinisikan function
def coba():
    print('ini adalah function')


# memanggil function
coba()

print('=' * 68)

# function sederhana , memnggil function didalam function


def suaraayam():
    print('kokokbetook!!!')


def hargaayam():
    suaraayam()
    print('harga ayam per 1 kg adalah Rp.15.000')


hargaayam()

# membuat function dengan input argument


def hargatotal(ayam):
    harga = 20000
    hargaTotal = ayam * harga
    print('harga satu ayam', harga, 'jika membeli',
          ayam,  'ayam. Maka total harga semua adalah', hargaTotal)


hargatotal(5)
hargatotal(1.5)
hargatotal(0.5)
hargatotal(0.25)
