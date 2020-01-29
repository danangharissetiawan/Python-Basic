# Input Output file

# MODE
# 1 ) w : write mode (mode menulis dan menghapus file lama,
#         jika tidk ada file lama maka akan dibuat file baru)
# 2 ) r : read mode only (hanya membaca)
# 3 ) a : appending mode (menambahkan data di akhir baris)
# 4 ) r+ : write and read mode


# Membuat file text
file = open("data.txt", 'w')  # 2 argumen : 1 ) nama file. 2 ) mode

file.write("File dari Python")
file.write("\nbaris ke dua")
file.write("\nbaris ke tiga")
file.write("\nbaris ke empat")

file.close()

# Membaca file text
file2 = open("data.txt", 'r')

# print(file2.read(20))  # opsional parameter : banyaknya karakter

print(file2.readline())  # membaca baris perbaris

file2.close()

# Appending mode
file3 = open("data.txt", 'a')

file3.write("\nbaris ini dibuat dengan mode append")

file3.close()
