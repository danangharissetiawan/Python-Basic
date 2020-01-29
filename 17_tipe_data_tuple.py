# tipe data list : tipe data yang bisa di manupulasi/dirubah
# tipe data tuple : tipe data yang fixs tidak bisa dirubah
# untuk melihat tipe data nya itu apa bisa menggunakan method( type()).

# list
import timeit
import sys
genap = [2, 4, 6, 8, 10]

# tuple
ganjil = (1, 3, 5, 7, 9)

# melihat type data
print(type(genap))
print(type(ganjil))


# untuk melihat apa yang bisa dilakukan dengan tipe data tersebut bisa menggunakan dir()

# print(dir(genap))
# print(dir(ganjil))

# kelebihan tuole dari list adalah tuple lebih ringan

# melihat besar memori yang dipakai dan waktu unruk memproses list dan tuple
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'sandika galih',
             'kang pukis', 'Danang haris ', "gedang goreng", "rokok surya", True, False, 1.15]

data_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 'sandika galih',
              'kang pukis', 'Danang haris ', "gedang goreng", "rokok surya", True, False, 1.15)

# melihat besar memori yang dipakai

besar_datalist = sys.getsizeof(data_list)
besar_datatuple = sys.getsizeof(data_tuple)

print('besar data list: ', besar_datalist)
print('besar data tuple: ', besar_datatuple)

# melihat waktu yang dibutuhkan u/ memroses data


waktu_datalist = timeit.timeit(stmt="[1,2,3,4,5,6,7,8]", number=1000000)
waktu_datatuple = timeit.timeit(stmt="(1,2,3,4,5,6,7,8)", number=1000000)

print('waktu untuk memroses list:', waktu_datalist)
print('wakru untuk memroses tuple', waktu_datatuple)
