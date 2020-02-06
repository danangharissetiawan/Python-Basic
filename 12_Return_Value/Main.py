# Fungsi dengan return value
def kuadraat(nilai):
    hasil = nilai ** 2
    print("Nilai kudrat dari", nilai, " = ", hasil)
    return  hasil

a = kuadraat(10)
print('='* 50)

# Fungsi dengan return value dan multiple argument
def kali(nilai1, nilai2):
    hasil = nilai1 * nilai2
    print("hasil dari ", nilai1, " * ", nilai2, " = ", hasil)
    return hasil

b = kali(5,10)

def tambah(nilai1, nilai2):
    hasil = nilai1 + nilai2
    print("hasil dari ", nilai1, " + ", nilai2, " = ", hasil)
    return hasil

c = tambah(5,5)
e = b + a
print("hasil dari ", b, " + ", a, " = ", e)
f = kuadraat(2) + kali(2,5) + tambah(10,5)
print(f)