number = 21
print('number =', number)

angka = 25
print('angka =', angka)

# u/ mempoliritaskan bilangan (value1 = nilai awal, value2 = nilai akhir, value3 = increment).
for i in range(0, 30, 5):
    print(i)
    if i is number:
        print('angka', i, 'ditemukan')
    elif i is angka:
        print('angka', number, 'tidak ditemukan')
else:
    print('Masih termasuk for, berada diakhir')

print('space diluar for')
