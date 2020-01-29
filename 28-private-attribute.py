# Attribute private / visibility private berguna untuk membatasi akses.
# ketika suatu visibility private di berikan kepada variabel/method tertentu
# Maka method / variabel tersebut tidak bisa di akses diluar class nya.


class mahasiswa():
    __nilai = 0
    __nilaiRataRata = 50

    def __init__(self, input_nama, input_nip):
        self.nama = input_nama
        self.nim = input_nip

    def uts(self, input__nilai):
        self.__nilai += input__nilai

    def uas(self, input__nilai):
        self.__nilai += input__nilai

    def status_siswa(self):
        if self.__nilai <= self.__nilaiRataRata:
            print(self.nama, '=', self.__nilai, 'tidak lulus')
        else:
            print(self.nama, '=', self.__nilai, 'lulus')


wowok = mahasiswa('Ahmad Bayu', 12345)
tengek = mahasiswa("Nur Irvan", 23456)

wowok.uts(15)
wowok.uas(45)
wowok.status_siswa()

tengek.uts(10)
tengek.uas(20)
tengek.status_siswa()
