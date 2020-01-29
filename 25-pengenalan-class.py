# class : *) sebuah template / blue print untuk membuat instance dari object
#         *) mendefinisikan object
#         *) menyimpan data dan perilaku yang disebut dengan properti & method


class mahasiswa():              # Bentuk sederhana dari class
    nama = 'nama',              # properti dari class
    pekerjaan = 'pekerjaan'


wowok = mahasiswa()             # cara menginstance class
tenggek = mahasiswa()

# mengganti nilai dari properti bisa dilakukan setelah di instance
wowok.nama = 'Ahmad Bayu Hidayatullah'
wowok.pekerjaan = 'Pelajar'

tenggek.nama = 'Nur Irfan'


print(tenggek.nama)
print(tenggek.pekerjaan)
print(wowok.nama)
print(wowok.pekerjaan)
