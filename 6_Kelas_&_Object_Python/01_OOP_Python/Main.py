'''
Object Oriented Programming(OOP) adalah cara terbaik dalam penulisan kode program yang bersar.
OOP memiliki 3 dasar topik utama:
    1- Warisan -> proses menggunakan detail dari kelass baru tanpa merubah kelas yang asli
    2- Enkapsulasi -> menyembunykan detail pribadi suatu kelas dari object lain
    3- Polimorfisme -> Konsep menggunakan operasi umum dalam berbagai cara untuk input data yang berbeda.
'''
class Siswa:
    # Atribut kelas
    jenis = "Mahasiswa"

    def __init__(self,nama, umur, jurusan, kelamin):
        self.jurusan = jurusan
        self.nama = nama
        self.umur = umur
        self.kelamin = kelamin

# Instance object
sherlock = Siswa("Sherlock", 20, "Detektif", "laki-laki")
putri = Siswa("Putri", 18, "Informatika", "perempuan")

print("{} adalah {} berjenis kelamin {} berumur {} jurusan {}".format(sherlock.nama, sherlock.__class__.jenis, sherlock.kelamin, sherlock.umur, sherlock.jurusan))

print("{} adalah {} berjenis kelamin {} berumur {} jurusan {}".format(putri.nama, putri.__class__.jenis, putri.kelamin, putri.umur, putri.jurusan))

'''
Method => Fungsi yang di definisikan didalam tubuh kelas, yang digunakan untuk mendefinisikan
          perilaku dari suatu object.
'''
class Orang:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    
    def hobi(self, hobi):
        return hobi

    def alamat(self, alamat):
        return alamat

conan = Orang("Conan", "Mahasiswa")

a = conan.hobi("menganalisa")
b = conan.alamat("Jepang")
print("\n{} adalah seorang {} yang tinggal di {}, dia memiliki hobi {}\n".format(conan.nama, conan.pekerjaan, b, a))



'''
Warisan => cara menciptakan kelas baru yang menggunakan data dari kelas yang ada tanpa merubahnya.
           kelas yang baru dibentuk adalah kelas turunan(kelas anak), sedangkan kelas yang sudah ada adalah kelas dasar(kelas parent)
'''
class Pria:
    def __init__(self):
        print("Pria adalah salah satu jenis manusia ciptaan tuhan")
    
    def watak(self, watak):
        return watak

    def sikap(self):
        sikap = "pekerja keras"
        return sikap


class Wanita(Pria):
    def __init__(self, nama):
        super().__init__()
        self.nama = nama
        print("Wanita adalah kaum sempalan tulang rusuk dari pria")

    def sikap(self):
        sikap = "lemah lembut"
        return sikap

silfi = Wanita("Silfi")
c = silfi.watak("egois dan percaya diri")
print("{} memiliki watak {} dan sikap {}\n".format(silfi.nama, c, silfi.sikap()))

arthur = Pria()
print("Arthur memiliki watak {} dan bersikap {}\n".format(arthur.watak("tekun dan teliti"), arthur.sikap()))



'''
Enkapsilasi => membatasi akses ke method dan variabel, untuk mencegah data dari modeifikasi langsung.
'''
class Harga:
    def __init__(self):
        self.__harga = 150.000

    def jual(self):
        print("dijual dengan harga {}".format(self.__harga))

    def setharga_max(self, harga):
        self.__harga = harga


baju = Harga()
baju.jual()

baju.__harga = 100
baju.jual()

baju.setharga_max(200)
baju.jual()



'''
Polimorfisme => kemampuan(dalam OOP) untuk menggunakan antarmuka umum untuk berbagai bentuk(tipe data)
'''
print("\n")
class Beo:
    def terbang(self):
        print("Beo dapat terbang")
    
    def berenang(self):
        print("Beo tidak dapat berenang")

class Penguin:

    def terbang(self):
        print("Penguin tidak dapat terbang")
    
    def berenang(self):
        print("Penguin dapatberenang")

# common interface
def tes_terbang(burung):
    burung.terbang()

#instantiate objects
blu = Beo()
peggy = Penguin()

# passing the object
tes_terbang(blu)
tes_terbang(peggy)