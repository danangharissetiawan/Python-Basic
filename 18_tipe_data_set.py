# tipe data set / himpunan : tidak tergantung pada ukuran dan frekuensi
# Ada 2 cara:

# 1) Menggunakan keyword set()
himpunan = set()

himpunan.add('pkn')
himpunan.add('penjas')
himpunan.add('matematika')
himpunan.add('bahasa indonesia')
himpunan.add('bahasa inggrish')
print(himpunan)
print(sorted(himpunan))

# 2) Menggunakan kurung kurawal {}
genap = {2, 4, 6, 8, 10}
ganjil = {1, 3, 5, 7, 9, }
prima = {2, 3, 5, 7}

buku = {'fiksi', 'religi', 'politik', 'ebook', 'komputer'}
teknologi = {'oppo', 'samsung', 'xiomi', 'vivo', 'ebook', 'komputer'}

print(genap)

# unicon() : untuk menggabungkan set
print(ganjil.union(genap))
print(buku.union(teknologi))

# intersection() : untuk membuat irisan
print(ganjil.intersection(prima))
print(buku.intersection(teknologi))
