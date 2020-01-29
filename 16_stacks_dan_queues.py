# stacks : mengambil data yang paling akhir dengan .pop()

from collections import deque
tumpukan = [1, 2, 3, 4, 5, 6]
print('data asal', tumpukan)

tumpukan.append(7)
print('data ditambahkan', 7)
print('data sekarang menjadi', tumpukan)

stack = tumpukan.pop()
print('data yang di ambil', stack)
print('data setelah diambil menjadi', tumpukan)

# untuk mengambil data yang awal dibutuhkan module

# cara menggunakan module : form collections import library yang ingin diimport


antrian = deque([1, 2, 3, 4, 5])
print('data asal', antrian)

antrian.append(6)
print('data yang ditambahkan', 7)
print('data setelah ditambahkan', antrian)
antrian.appendleft(0)
print('data yang ditambhkan', 0)
print('data setelah ditambahkan', antrian)

out = antrian.popleft()
print('data keluar', out)
print('data sekarang menjadi', antrian)

out = antrian.popleft()
print('data keluar', out)
print('data sekarang menjadi', antrian)
