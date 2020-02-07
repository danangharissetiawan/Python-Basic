'''
- Fungsi Lambda adalah sebagai fungsi anonim kecil.
- Fungsi lambda dapat mengambil beberapa argument, tetapi hanya dapat memiliki satu ekpresi
- Sintaks:
    lambda argument : ekspresi

'''
# menambahkan argument dengan 10
x1 = lambda a : a + 10
print(x1(5))

# Fungsi lambda mengambil beberapa argument
x2 = lambda b, c : b * c
print(x2(2,3))

'''
Mengapa menggunakan fungsi lambda?
- fungsi lambda sebaiknya digunakan sebagai fungsi anonim didalam fungsi lain.
- contoh: ketika anda mendefinisikan fungsi yang memiliki satu argument,
          dan argument itu akan dikalikan dengan angka yang tidak dikenal:
'''

def kali(n):
    print(n)
    return lambda e : e * n

kalilambda = kali(5) # argument untuk fungsi kali

print(kalilambda(10)) # argument untuk lambda

