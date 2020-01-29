# Error dalam pemrograman ada 2 :
# 1) Error sintaks : error yang bisa dideteksi oleh intrepeter/program.
# 2) Error runtime

# 1) Error sintaks

# print("Hallo Dunia)

# 2) Error runtime

# angka = int(input("Masukan angka sembarang\n")) # ketika selain angka dimasukan akan terjadi error runtime

# print(angka)

# def pembagian(a,b):
#     return a/b
#
# penyebut = int(input("masukan angka penyebut\n"))
# pembilang = int(input("masukan angka pembilang\n"))
#
# print(pembagian(penyebut,pembilang))


# kenapa belajar ini ??

# karena program ketika mengalami error di tengah-tengah maka program akan keluar saat itu juga
# sehingga kita harus bisa mengheandling error tersebut, agar program tetap berjalan dan errornya di lompari
# error heandling dengan try dan exceptcion
while True:
    try:
        def pembagian(a,b):
            return a/b

        penyebut = int(input("masukan angka penyebut\n"))
        pembilang = int(input("masukan angka pembilang\n"))

        print(pembagian(penyebut,pembilang))
        break
    # except ValueError:
    #     print("yang anda masukan bukan angka\n")
    # except ZeroDivisionError:
    #     print("angka pembilang yang anda masukan nol, pilih yang lain yaa gays!!\n")

    # Atau lebih mudahnya :
    except Exception as ex:
        print(ex)
print("diluar program")


# Type of exception errors
# 1. IOError
# 2. ImportError
# 3. ValueError
# 4. ZeroDivisionError
# 5. KeyboardInterrupt
# 6.EOFError


