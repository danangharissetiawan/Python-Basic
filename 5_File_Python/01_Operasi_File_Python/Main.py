'''
- File adalah sesuatu yang berlokasi disk untuk menyimpan informasi terkait.
  Ini digunakan untuk menyimpan data secara permanen dalam memori yang tidak mudah menguap (mis. Hard disk).

- Karena, random access memory (RAM) volatile yang kehilangan datanya ketika komputer dimatikan,
  kami menggunakan file untuk penggunaan data di masa depan.

- Ketika kita ingin membaca dari atau menulis ke file kita harus membukanya terlebih dahulu.
  Ketika kita selesai, itu harus ditutup, sehingga sumber daya yang terikat dengan file dibebaskan.

- Operasi pada file dapat dilakukan menggunakan python dengan urutan sebagai berikut:
  1 - Buka File
  2 - Buka Atau Tulis(Modifikasi File)
  3 - Tutup File

- Kita bisa menentukan mode saat membuka file:
    --> Mode <--              --> Deskripsi <--
        'r'        --> 	Buka file untuk dibaca. (default)
        'w'        -->  Buka file untuk ditulis. Membuat file baru jika tidak ada atau memotong file jika ada.
        'x'        -->  Buka file untuk pembuatan eksklusif. Jika file sudah ada, operasi gagal.
        'a'        -->  Buka untuk menambahkan di akhir file tanpa memotongnya. Membuat file baru jika tidak ada.
        't'        -->  Buka dalam mode teks. (default)
        'b'        -->  Buka dalam mode biner.
        '+'        -->  Buka file untuk memperbarui (membaca dan menulis)

        - Standarnya adalah membaca dalam mode teks. Dalam mode ini, 
          kita mendapatkan string ketika membaca dari file.

        - Di sisi lain, mode biner mengembalikan byte dan ini adalah 
          mode yang akan digunakan ketika berurusan dengan file non-teks seperti file gambar atau exe.
'''

# Membuka file
a = open("test.txt")
a = open("test.txt", 'w')
a = open("test.txt", 'r+b')
a.close()

# ketika bekerja dengan file dalam mode teks, sangat disarankan untuk menentukan jenis penyandian.
d = open("test.txt", mode = 'r', encoding = 'utf-8')
d.close()

# Menutup file
e = open("test.txt", encoding = 'utf-8')

e.close()  #methode ini tidak sepenuhnya aman
# --> untuk lebih aman bisa menggunakan blok
try:
    f = open("test.txt", encoding='utf-8')
    # lakukan operasi pada file
finally:
    f.close()

# membuka file dengan with --> cara ini lebih aman karena dilakukan secara internal.
with open("test.txt", encoding='utf-8') as g:
    # lakukan operasi pada file
    pass

# Menulis di file menggunakan python
with open("text.txt", 'w', encoding='utf-8') as h:
    h.write("Hallo Dunia!")
    h.write("\nbaris kedua\n")
    h.write("baris ketiga\n")
    h.write("baris keempat")
# Ketika ingin membuat baris baru, harus menyertakan karakter baris baru.

i = open("text.txt", 'r', encoding='utf-8')
print(i.read(10))
print(i.read())
print(i.tell()) # melihat posisi crusor
print(i.seek(6)) # mengubah posisi crusor
print(i.read())
i.close()


print("=" * 50)


# Membaca baris dem baris file menggunakan loop
f = open("text.txt", 'r', encoding='utf-8')
for baris in f:
    print(baris, end='')  # end ="akhir baris"
f.close()

print("\n")
print("="*50)

# Kita juga bisa membaca setiap barisnya menggunakan readline()
f = open("text.txt", 'r', encoding='utf-8')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

f.close()

print("="*50)
f = open("text.txt", 'r', encoding='utf-8')
print(f.readlines())


'''
Method file
close()                     --> Tutup file yang terbuka. Tidak berpengaruh jika file sudah ditutup.
detach()	                --> Pisahkan buffer biner yang mendasarinya dari TextIOBasedan kembalikan.
fileno ()	                --> Kembalikan nomor integer (deskriptor file) file.
flush()	                    --> Siram buffer tulis dari aliran file.
isatty()                    --> Kembali Truejika aliran file bersifat interaktif.
read(n)	                    --> Baca maksimal n karakter membentuk file. 
                                Membaca hingga akhir file jika negatif atau None.
readable()	                --> Kembali Truejika aliran file dapat dibaca.
readline(n=-1)	            --> Baca dan kembalikan satu baris dari file. 
                                Dibaca paling banyak n byte jika ditentukan.
readlines(n=-1)	            --> Baca dan kembalikan daftar garis dari file. 
                                Dibaca paling banyak n byte / karakter jika ditentukan.
seek(offset,from=SEEK_SET)	--> Ubah posisi file menjadi ofset byte, dengan mengacu dari (mulai, saat ini, akhir).
seekable()	                --> Kembali Truejika aliran file mendukung akses acak.
tell()	                    --> Mengembalikan lokasi file saat ini.
truncate(size=None)	        --> Ubah ukuran aliran file ke ukuran byte. Jika ukuran tidak ditentukan,
                                ubah ukuran ke lokasi saat ini.
writable()	                --> Kembali Truejika aliran file dapat ditulis ke.
write(s)	                --> Tulis string s ke file dan kembalikan jumlah karakter yang ditulis.
writelines(line)	        --> Tulis daftar baris ke file.
'''
