# List memilki keyword bantuan untuk memaksimalkan fungsi dari list.


buah = ['apel', 'mangga', 'jeruk', 'anggur', 'pisang', 'durian', 'pepaya', 'rambutan']

# len() --> untuk menghitung banyak item didalam list
print(len(buah))

# index() --> mengetahui suatu item di urutan ke berapa dalam list.
c = buah.index("mangga")
print(c)

# append() --> untuk menambahkan item diakhir list
a = buah.append('timun')
print(buah)

# remove() --> untuk menghapus tidak mengembalikan item tertentu
b = buah.remove('timun')
print("yang remove = ", b) # mengembalikan nilai none
print(buah)

# pop() --> menghapus dan mengembaalikan item tertentu (atau item terakhir jika index tidak ditemukan)
c = buah.pop(1)
print("yang di pop = ", c)
print(buah)

d = buah.pop()
print("yang di pop = ", d)
print(buah)

# del --> untuk menghapus item dengan index yang ditentukan atau semua item
del buah[2] # anggur dihapus
print(buah)

# clear() --> untuk mengkosongkan list
buah.clear()
print(buah) # list buah menjadi kosong

buah1 = ['apel', 'mangga', 'jeruk', 'anggur', 'pisang', 'durian', 'pepaya', 'rambutan']

# copy() --> untuk menyalin list
buah2 = buah1.copy()
print(buah2)

#list() --> juga untuk menyalin list
buah3 = list(buah2)
print(buah3)

#insert() --> menambahkan item dengan posisi yang spesifik.
buah1.insert(1,"jeruk") # --> menambahkan item jeruk di index ke satu
print(buah1)

#count() ---> menghitung ada berapa item yang sama dalam satu list
a = buah1.count("jeruk") # ---> jeruk dalam list buah1 muncul berapa kali
print(a)

#sort() --> mengurutkan list
buah1.sort()
print(buah1)

#reverse() --> mengembalikan urutan penyortiran list.
buah1.reverse()
print(buah1)



# ---- Mengabungkan list dengan list, list dengan tuple, dan list dengan set ----
list_a = [4,5,6]
list_b = ["anggur"]
for x in list_b:
    list_a.append(x)
print(list_a)

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]
data_tuple = {'jeruk', 'anggur', 'nanas'}
data_set = ("buku", "polpen", "papan tulis")

list1.extend(list2) # menggabungkan dua list menggunakan extend
print(list1)

data_list1 = list1 + list2 # menggabungkan dua list menggunakan +
print(data_list1)

list1.extend(data_tuple) # menggabungkan list dengan tuple menggunakan extend
print(list1)

list1.extend(data_set) # menggabungkan list dengan set menggunakan extend
print(list1)

# Membuat list dengan Elegan
angka = [2** x for x in range(10)]
print(angka)