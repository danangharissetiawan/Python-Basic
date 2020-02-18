# List Comprehension vs For Loop dengan Python

# Contoh 1 --> Iterasi string dengan for loop
manusia = []
for tambah in "manusia":
    manusia.append(tambah)
print(manusia)
# Contoh 2 --> Iterasi string dengan list comprehenson
orang = [nama for nama in "sherlock"]
print(orang)


# List Comprehensions vs Lambda functions

# Contoh 1 --> Menggunakan fungsi lambda di dalam list
buah = list(map(lambda x: x, "anggur"))
print(buah)
# Contoh 2 --> Menggunakan if dengan list comprehension
angka = [x for x in range(20) if x % 2 == 0]
print(angka)


#  Nested IF dengan List Comprehension
nes_angka = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(nes_angka)

# if else dengan list comprehension
gg = ["Genap" if i % 2 == 0 else "Ganjil" for i in range(10)]
print(gg)

# Nested loop di dalam list comprehension

# Contoh 1 --> Tranpose matrix menggunakan nested loop
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

# Contoh 2 --> Transpose matrix menggunakan list comprehension
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)

'''
<--- Poin Poin Penting --->
- Pemahaman daftar adalah cara yang elegan untuk mendefinisikan dan membuat daftar berdasarkan daftar yang ada.
- Pemahaman daftar umumnya lebih kompak dan lebih cepat dari fungsi normal dan loop untuk membuat daftar.
- Namun, kita harus menghindari penulisan daftar yang sangat panjang dalam satu baris
  untuk memastikan bahwa kode tersebut mudah digunakan.
- Ingat, setiap pemahaman daftar dapat ditulis ulang untuk loop, 
  tetapi setiap untuk loop tidak dapat ditulis ulang dalam bentuk pemahaman daftar.


  -------------------------------> Keep smile for awesome :) DaRisset <------------------------------------------
'''

