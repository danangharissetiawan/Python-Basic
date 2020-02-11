'''
* Tuple pada python mirip dengan list.
  perbedaan antara keduanya adalah kita tidak bisa mengubah element tupel setelah ditetapkan,
  sedangkan dalam list element dapat di ubah.

  - Membuat Tuple
    * sebuah tuple dapat di buat dengan menempatka semua item di dalam tanda (), dipisahkan dengan koma(,).
    * tanda () hanyalah opsional, tapi dalam praktiknya kita disarankan untuk emnggunakannya.
    * tuple dapat mengandung sejumlah item yang mungkin memiliki jenis berbeda seperti: integer, string, float dll.
'''

#  =========> Membuat Tuple <=========
# Contoh:
# Tuple dengan tanda kurunt ()
a1 = (1,2,3)
b1 = ('jeruk', 'anggur', 'pisang')
print(a1)
print(b1)

# Tupel tanpa tanda kurung ()
a2 = 4,5,6
b2 = 'buku', 'pena', 'penghapus'
print(a2)
print(b2)

# Tupel dengan item yang jenisnya berbeda
a3 = (1, 2.5, "pisang")
b3 = 10, "jeruk", 0.5
print(a3)
a, b, c = a3
print(a)
print(b)
print(c)
print(b3)

# Tuple bersarang (nested tuple)
c1 = ("jogja", ['jogja 1', 'jogja 2', 'jogja 2'])
print(c1)

# Membuat tuple dengan satu element/item agak sulit, karene kita harus memberikan tanda koma(,)
a4 = ("hello")
print(type(a4))  # Ini bukan tuple tapi string

b4 = ("hello",)
print(type(b4))  # Ini baru tuple

# =======> Mengakses Tuple <=======
# Pengindeksan
'''
- item didalam tuple memiliki index yang dimuali dari 0 sampai jumlah yang sesuai dengan jumlah tuple.
- index harus berupa bilangan bulat.
- tuple bersarang (nested tuple) cara pen indeksannya juga bertingkat.
'''
print(b1[1]) # mengakses satu item
print(b1[1:])  # item index ke satu sampai item yang terakhir
print(b2[0:3])  # mengakses index ke 0, sampai 2
print(c1[1][1])  # mengakses tuple bersarang(nested tuple)
print(a1[-1])  # ini merujuk ke index terakhir, jika -2 merujuk index terakhir kedua, dan seterusnya.

# =======> Manipulasi Tuple <=======
'''
- memang kita tidak dapat mengubah tuple,
  tapi ketika elemen bersarangnya tuple merupakan list kita dapat mengubahnya.
'''
c2 = ('anggur', 'mangga', ['manis', 'asam', 'pahit'], [1, 2, 3, 4])
print(c2)
c2[2][2] = 'pedas'
print(c2)

# Menggabung tuple
print(a1 + b1)

# Mengulang element-element tuple untuk beberapa kali
c3 = ("Dunia",) * 3
print(c3)

# Menghapus Tuple
'''
- sebelumnya sudah kita bahas bahwa kita tidak bisa menghapus tuple,
  tapi jika menghapus tuple sepenuhnya itu dimungkinkan dengan kata kunci del
'''
tuple_del = (1, 2, 3, 4, 5, 6, 7, 8, 9)
del tuple_del
# print(tuple_del) --> ini akan menghasilkan 'name tuple_del is not defined'


# =======> Keyword Tuple <=======
'''
Key untuk tuple hanya ada 2:
1 - count() ---> mengembalikan jumlah item yang sama dalam tuple
2 - index() ---> mengembalikan index item yang pertama sampai dengan yang ke x
'''
print(b1.count('jeruk'))
print(b1.index('jeruk'))


# =======> Operasi lain yang bisa dilakukan pada tuple <=======
# 1- Tes keanggotaan Tuple (in)
hoby = ('musik', 'coding', 'membaca', 'menulis')
print('coding' in hoby)  # Mengembalikan boolean (True / False)

# 2- Iterasi pada tuple
nama = ('Wowok', 'Tarkom', 'Dobok', 'Jemblem')
for i in nama:
    print("Hallo nama saya", i)


'''
* Kelebihan tuple
- biasanya tuple digunakan untuk tipe data yang heterogen (berbeda) dan list tipe data homogen (sama)
- iterasi pada tuple lebih cepat dari pada daftar, karena data pada tuple tidak berubah.
- dengan element yang tidak bisa diubah, ini dapat kita gunakan sebagai kunci atau kamus seperti: username, password dll
- jika anda memiliki data yang tidak akan dirubah, sebaiknya anda menggunakan tuple,
  karena bisa menjamin bahwa data aman dari penulisan.
'''


# ========================> Keep Coding For Awesome :) <=================================