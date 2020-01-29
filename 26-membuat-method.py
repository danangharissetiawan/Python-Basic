# Method : sesuatu sesuatu yang merepresentasikan data/keadaan dari sebuah object
#          fungsi yang berada didalam class


# class
class mahasiswa():
    nama = 'nama'

    def belajar(self, kondisi):     # ini method
        print(self.nama, 'sedang belajar dengan', kondisi)

# NB : self : untuk mengambil properti didalam class yang bersangkutan dengan yang dibuat instansi


# Main program
wowok = mahasiswa()  # object/instance-nya
tengek = mahasiswa()

wowok.nama = 'Wowoktek siketek'
tengek.nama = 'Nur Irfan'

wowok.belajar('giat')
tengek.belajar('tidur dan malas-malasan')
