'''
* Pengenalan String:
    - string adalah susunan karakter, dan karakter adalah simbol.
    - sebenarnya komputer tidak berurusan dengan karakter, komputer hanya berurusan dengan biner.
      sebenarnya karakter" yang ada di layar itu adalah hasil konversi dari biner, kombinasi dari 0 sampai 1.
    - konversi dari karakter ke angka di sebut encoding, sedangkan sebaliknya disebut decoding.
    - ASCII dan Unicode adalah beberapa pengodean yang populer digunakan.
    - dalam python string adalah susunan dari karakter Unicode.
    - Unnicode diperkenalkan untuk memasukan setiap karakter bahasa dan membawa keseragaman dalam pengodean.
    - pelajari unicode lebih lanjut (https://docs.python.org/3.3/howto/unicode.html).
'''

# Membuat string:
print('hallo')
print("hallo")
print('''hallo''')

# Mengakses karakter String:
my_str = "darisset"
print(my_str[0])
print(my_str[3:]) # index ke 3 - akhir
print(my_str[:5])   # indek awal(0) sampai ke 5
print(my_str[1:5])  # index 1 - 5
print(my_str[-2])  # index ke kedua dari akhir

# Mengubah dan Menghapus String:
    # Kita tidak dapat mengubah kemponen string jika telah ditetapkan,
    #  tapi kita bisa mengganti string dengan string yang baru.
a = 'python2'
a = 'python3'
print(a)
    # kita tidak bisa mengapus karakter string, tertapi kita bisa menghapus setring dengan sepenuhnya. dengan del
del a
# print(a) --> ini jika di tampilkan akan mendapati error.

# Operasi String
a = 'hallo'
b = 'dunia'
print(a + b)
print('i am'
' sherlock holmes')  # () untuk membuat srting berbeda baris.

# - iterasi string:
c = 'Hallo Dunia!'
hitung = 0
for karakter in c:
    hitung += 1
print(c, "terdiri dari", hitung, "karakter")

# - tes keanggotaan string (in / not in)
d = 'sherlock holmes'
e = 'h' in d
e2 = 'h' not in d
print(e) # True 
print(e2)  # False


# - Encapse Karakter (Karakter ilegal dalam string)
# \' = kutipan tunggal
# \" = kutipan ganda
# \\ = backslash
# \n = new line
# \r = carringe return
# \t = tab
# \b = backspache
# \f = from field
# \ooo = oktal value
# \xhh = hex value


# Method String: --> semua string dibawah mengembalikan nilai baru, bukan string asli


#  capitalize() = mengubah karakter pertama menjadi besar
str1 = "sherlock holmes"
print(str1.capitalize())
# casefold() = mengubah string menjadi huruf kecil
str2 = "SHERLOCK HOLMES"
print(str2.casefold())
# center(ruang default) = menampilkan string di tengah sesuai nilai dari center
print(str1.center(100))
# count() = menghitung satu karakter/ kata muncul dalam satu string
print(str1.count('h'))
print(str1.count('h', 5, 10))  # 1 - string yang akan di cari 2 - awal tempat pencarian 3 - akhir tempat pencarian
# encode() = mengkodekan string
print(str1.encode(encoding="ascii", errors="ignore"))
# endwith() = mengembalikan nila true jika string berakhir dengan nilai yang ditentukan.
print(str1.endswith("s"))
# expandtabs() = akur ukuran tab string
str3 = "hello\tDunia!"
print(str3.expandtabs(4))
# --> Method umum string --> lower() upper() join() format() find() replace() split()
# lower() = mengembalikan strng dengan huruf kecil
# upper() = emngembalikan string huruf besar
# join() = mengembalikan string gabungan
# format() = memformat string agar tampilan lebih bagus
# find() = mengembalikan indeks kemunculan substring yang pertama
# replace() = mengganti inside substring
# split() = membagi string dari kiri


