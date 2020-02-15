'''
Dictionary: - Tipe data yang mengandung element-element tidak teratur.
            - dictionary memiliki kunci: pasangan nilai.
'''
rokok = {"surya": 18000, "sukun": 14000, "LA": 15000}
print(rokok)
print(rokok["surya"])

rokok["mlinjo"] = 12000
print(rokok)

del rokok["sukun"]
print(rokok)
print(list(rokok))
print(sorted(rokok))

print("sukun" in rokok)
print("sukun" not in rokok)

# Membuat dictionary dengan kata kunci dict.
nama = dict([("Sherlock", 180), ("Holmes", 175), ("Conan", 140), ("Doyle", 160)])
print(nama)

buah = dict(apel=1, anggur=2, mangga=3, durian=4)
print(buah)

# Membuat dictionari denggan mudah
n = {x: x ** 2 for x in (2, 3, 4)}
print(n)

# Method dictionary
'''
clear()             --> Hapus semua item dari kamus.
copy()	            --> Kembalikan salinan kamus yang dangkal.
fromkeys(seq[, v])  --> Kembalikan kamus baru dengan kunci dari seq dan nilai sama dengan v (default ke None).
get(key[,d])	    --> Kembalikan nilai kunci . Jika kunci tidak keluar, kembalikan d (default ke None).
items()	            --> Kembali tampilan baru dari item kamus (kunci, nilai).
kunci ()	        --> Kembali tampilan baru dari kunci kamus.
pop(key[,d])	    --> Hapus item dengan kunci dan kembalikan nilainya atau d jika kunci tidak ditemukan. Jika d tidak disediakan dan kunci tidak ditemukan, naikkan KeyError.
popitem()	        --> Hapus dan kembalikan item arbiter (kunci, nilai). Naik KeyErrorjika kamus kosong.
setdefault(key[,d])	--> Jika kunci ada di kamus, kembalikan nilainya. Jika tidak, masukkan kunci dengan nilai d dan kembalikan d (default ke None).
update([other])	    --> Perbarui kamus dengan pasangan kunci / nilai dari pasangan lain , timpa kunci yang ada.
values()	        --> Kembali tampilan baru dari nilai-nilai kamus
'''

# funsi bawaan python dictionary
'''
all()       --> Kembali Truejika semua kunci kamus benar (atau jika kamus kosong).
any()       --> Kembali Truejika ada kunci kamus yang benar. Jika kamus kosong, kembaliFalse.
len()       --> Kembalikan panjang (jumlah item) dalam kamus.
cmp()       --> Membandingkan item dari dua kamus.
sorted()    --> Kembalikan daftar kunci yang diurutkan dalam kamus.
'''