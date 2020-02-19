data = [1, 2, 3, 4, 5]
data2 = [10, 20, 30, 40, 50]

# mengakses list
print('mengakses list')
sd1 = data[2]
print(sd1)
sd2 = data[-4]
print(sd2)
print('='*10)

# memotong list
print('memotong list')
sd3 = data[2:4]
print(sd3)
sd4 = data[:3]
print(sd4)
print('='*10)

# menambah list
print('menambah list')
data3 = data + data2
print(data3)
print('='*10)

# merubah content dari list
print('merubah content dari list')
data[2] = 6
print(data)
print('='*10)

# mengcopy list ke variabel baru
print('mengcopy list kevariabel baru')
a = data[:]
a[3] = 50
print(a)
print('='*10)

# list dalam list
print('list dalam list')
x = [data, data2]
print(x)
print('='*10)

# mengakses list dalam multidimensional list
print('mengakses list dalam multidimensi list')
y = x[1][4]
print(y)
print('='*10)

# merubah list dengan metode slicing
print('merubah list dengan metode slicing')
data[1:3] = [5, 6]
print(data)
print('='*10)

# method untuk list
print('method untuk list')
data.append(20)
print(data)
print('='*10)
