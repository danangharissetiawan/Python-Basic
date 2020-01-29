# while : adlh key looping.
# * memiliki nilai awal
# * memiliki kondisi terminasi
# * memiliki increment
luar = 'ini diluar looping'

# integer
angka = 0
while angka <= 5:
    print('sekarang angka', angka)
    angka = angka + 1

print(luar)

# bolean
status = True
angka = 0
while status:
    print('status sekarang adalah', status)
    if angka == 5:
        status = False
        print('status sekarang adalah', status)
    angka += 1

print(luar)

# while else, break, continue, pass

# else
i = 0
while i < 10:
    print('nilai saat ini adalah', i)
    i += 1
else:
    print('nilai diakhir while adalah', i)

print(luar)

# break
i = 0
while i < 10:
    if i == 5:
        break
    print('nilai saat ini adalah', i)
    i += 1
else:
    print('nilai diakhir while adalah', i)

print(luar)

# continue
i = 0
while i < 10:
    if i == 5:
        print('cekpoint 1 adalah', i)
        i += 1
        continue  # hati" dengan continue didalam while.
    print('nilai saat ini adalah', i)
    i += 1
else:
    print('nilai diakhir while adalah', i)
print(luar)

# pass : sama saja :p
