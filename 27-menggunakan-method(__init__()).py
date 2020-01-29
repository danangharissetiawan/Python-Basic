# Method __init__() : Method yang otomatis dijalankan ketika class di instansiasi

# Class


class mahasiswa():

    var = ['nama', 'namaPendek', 'nomor', 'pekerjaan', 'hoby']

    def __init__(self, nama, nama_panggilan, nomor, pekerjaan, hobi):
        self.nama = nama
        self.namaPendek = nama_panggilan
        self.nomor = nomor
        self.pekerjaan = pekerjaan
        self.hobi = hobi
        self.var

    def getPro(self):
        return self.var

    def get_data(self):
        return self.nama, self.namaPendek, self.nomor, self.pekerjaan, self.hobi

    def hoby(self):
        print(self.nama, 'memiliki hobi', self.hobi)


# Main Program

wowok = mahasiswa('Ahmad Bayu Hidayatullah', 'Hida',
                  62898707577, 'Pelajar', 'Bermain Gitar')

print(wowok.get_data())
dataLengkap = wowok.get_data()
dataValue = wowok.getPro()


for i, (value, data) in enumerate(zip(dataValue, dataLengkap)):
    print(i, ')', value, '=', data)

print(wowok.hoby())
