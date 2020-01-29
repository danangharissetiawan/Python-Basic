# Method untuk manipulasi list

barang = ['buku', 'bolpoin', 'gitar', 'laptop', 'sepedah', 'mobil']
# 1- .append (): untuk menmbah list diakhir
barang.append('sepatu')
print(barang)

# 2- .extend() : untuk mengiterabel string yang ditambahkan pada list
barang.extend('rokok')
print(barang)

# 3- .insert(lokasi, list bary) : untuk menambahkan list dimanapun yang dikehendaki
barang.insert(2, 'meja')
print(barang)

# 4- .count() : untuk menghitung string/list

jumlahBarang = barang.count('sepatu')
print('Jumlah stok spstu adalah', jumlahBarang)

# 5- .remove() : untuk menghapus list
barang.remove('meja')
print(barang)
print('=' * 68)

# 6- .reverse() : untuk mereverse list.
barang.reverse()
print(barang)

print('=' * 68)

# 7- .copy() : untuk mengkopi list tanpa mempengaruhi listyang di copy

# tidak dengan copy
suft = barang
suft.append('kaos kaki')
print(suft)
print(barang)
# list yang ditambahkan di var suft akan masuk di var barang.

# menggunakan .copy()
alat = barang.copy()
alat.append('korek api')
print(alat)
print(barang)
