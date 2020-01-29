# List sebagai itereble
buah = ['anggur', 'apel', 'rambutan', 'jeruk', 'jambu', 'melon', 'semangka']

for b in buah:
    print(b)
    print(len(b))

a = '=' * 50
print(a)

# string sebagai itereble
apel = 'apel'

for i in apel:
    print(i)

a = '=' * 50
print(a)

# for didalam for
gorengan = ['tempe', 'bakwan', 'ote-ote', 'rempelas', 'pukis']
minuman = ['kopi', 'teh', 'air mineral', 'josua', 'capcin']

daftar_belanja = [buah, gorengan, minuman]

for sub_daftar_belanja in daftar_belanja:
    print(sub_daftar_belanja)
    for komponen in sub_daftar_belanja:
        print(komponen)
