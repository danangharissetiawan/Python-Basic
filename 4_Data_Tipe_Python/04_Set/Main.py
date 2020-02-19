'''
* Set:  - Himpunan item yang tidak teratur, setiap item bersifat unik dan tidak berubah.
        - Sehingga pengindekan tidak dapat digunakan.
        - tapi himpunan itu bisa burubah, bisa menghapus dan menghapus item.
        - Set dapat digunakan untuk melakukan operasi set matematis seperti union, persimpangan,
          perbedaan simetris dll.

* Membuat Set: - Satu set dibuat dengan menempatkan semua item (elemen) di dalam kurung kurawal {},
                 dipisahkan dengan koma atau dengan menggunakan fungsi bawaan set().
               - Element dari set boleh terdiri dari berbagai macam tipe data.
               - tetapi satu set tidak ada element yang bisa beruabah
'''

# Membuat set
a = {1, 2.4, "hello", "dunia"}
a1 = set([1,4])
print(a)
print(a1)

# mengubah set
a1.add(2)
print(a1)
a1.update([5,6])
a1.update([3,6],{7,9,8})
print(a1)

# Menghapus set
# dengan metode discard() dan remove()
a.discard("hello")
print(a)
a.remove("dunia")
print(a)
# Menghapus dengan pengembalian
a2 = a.pop()
print(a)
print(a2)
a.clear()
print(a) # kosong

# Operasi set
# 1 - union (pengabungan dua set hanya yang unik saja)
b = {1, 2, 3, 4, 5, 6, 7}
b1 = {8, 6, 7, 9, 10}
print(b | b1)
print(b.union(b1))
print(b1.union(b))
# 2 - set intersection (titik temu dua set yang memiliki element yang sama)
c = {1, 2, 3, 4, 5}
c1 = {6, 7, 3, 2, 1}
print(c & c1)
print(c.intersection(c1))
print(c1.intersection(c))
# 3 - difference (item yang ada di set 1 dan tidak ada di set 2)
d = {1, 2, 3, 4, 5}
d1 = {1, 3, 5, 6, 7}
print(d - d1)
print(d.difference(d1))
print(d1 - d)
print(d1.difference(d))
# 4 - symmetric_difference (mengecualikan element yang sama dari kedua set)
e = {1, 2, 3, 4, 5}
e1 = {3, 4, 6, 7, 8}
print(e ^ e1)
print(e.symmetric_difference(e1))
print(e1 ^ e)
print(e1.symmetric_difference(e))

# Method set python
'''
isdisjoint() --> Mengembalikan  Truejika dua set memiliki persimpangan nol.
issubset() -->	Kembali  Truejika set lain berisi set ini.
issuperset() --> Kembali  Truejika set ini berisi set lain.
copy() --> Mengembalikan salinan set.
'''
# Tes keanggotaan set
f = {"Sherlock Holmes", "Arthur Doyle", "Conan doyle", "Mitsuki yamato"}
print("Sherlock Holmes" in f)
print("Sherlock Holems" not in f)

# Iterasi dalam set
names = set(["Sherlock", "Holmes", "Conan", "Doyle", "Arthur"])
for i in names:
    print("Nama saya adalah ", i)

# Fungsi bawaan set
'''
all()	    --> Kembali Truejika semua elemen set benar (atau jika set kosong).
any()       --> Kembali Truejika ada elemen set yang benar. Jika set kosong, kembaliFalse.
enumerate() -->	Kembalikan objek enumerasi. Ini berisi indeks dan nilai semua item yang ditetapkan sebagai pasangan.
len ()      --> Kembalikan panjang (jumlah item) di set.
max ()      --> Kembalikan item terbesar di set.
min ()      --> Kembalikan item terkecil di set.
sorted()    --> Kembalikan daftar yang diurutkan baru dari elemen dalam set (tidak mengurutkan set itu sendiri).
sum()       --> Kembalikan jumlah semua elemen dalam set.
'''