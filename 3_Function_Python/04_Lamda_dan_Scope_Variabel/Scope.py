'''
- Variabel hanya berlaku di wilayah tempat variabel itu dibuat, hal ini disebut ruang lingkup variabel(scope variabel)
- Scope variabel ada 2:
    1 - Lokal = Variabel yang dibuat di dalam fungsi, hanya dapat digunakan di dalam fungsi itu.
    2 - Global = Variabel yang dibuat di tubuh utama code python,
                 Variabel Global tersedia didalam ruang lingkup apapun, baik global ataupun lokal.

'''

# Variabel Lokal
print("="*10," Variabel Lokal")
def myfunc():
    x = 50    # variabel local
    print(x)

myfunc()


def tambah(n):
    x = n + 10     # Variabel local
    def kali():
        hasil = x * 2
        print(x)
        print(hasil)
    kali()

#  print(x) variabel x tidak bisa diakses diluar fungsi

tambah(2)

# Variabel Global
print("="*10," Variabel Global")

z = 10

def cetak():
    print(z)

cetak()
print(z)

# NB: Jika anda memberi nama variabel di luar fungsi dan di dalam fungsi dengan nama yang sama,
#     maka python akan menganggap kedua variabel tersebut berbeda.

print("="*10, " Variabel Penamaan")
c = 100

def penamaan():
    c = 200
    print(c)

penamaan()
print(c)


'''
* NB: Kata Kunci Global
      1 - Jika anda ingin menjadikan variabel lokal bersifat global,maka anda bisa menggunakan keyword global.
      2 - jika anda ingin mengubah nilai variabel global didalam fungsi, anda juga bisa menggunakan keyword global.

'''
print("="*10, " kata Kunci Gobal")

# contoh 1
def lokal():
    global x1
    x1 = 20

lokal()
print(x1)

# contoh 2
x2 = 100
print(x2," belum di ubah")
def umum():
    global x2
    x2 = 50

umum()
print(x2, " setelah diubah")
