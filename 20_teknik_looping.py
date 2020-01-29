# teknik looping

# list dan Tuple
data_key = ['Nama', 'Nomor', 'Agama', 'Pekerjaan', 'Hobi', 'Alamat']

data_value = ['Danang Haris', 628817043533,
              'Islam', 'Mahasiswa', 'Coding', 'Tambakboyo']

# enumerate() : untuk memberi nomor didepannya saat di looping
for i, key in enumerate(data_key):
    print(i, '-', key)
print('='*101)

# zip() : untuk menggabngkan dua buah list
for i, (key, value) in enumerate(zip(data_key, data_value)):
    print(i, '-', key, '=', value)
print('='*101)

# Melooping set
makananKesukaan = {'Bebek bakar', 'Nasi goreng', 'Mie ayam', 'Bakso', 'Pizza'}
hargaMakanan = {23000, 11000, 7000, 6000, 50000}

for i, makanan in enumerate(sorted(makananKesukaan)):
    print(i, '-', makanan)
print('=' * 101)

for i, (makanan, harga) in enumerate(sorted(zip(makananKesukaan, hargaMakanan))):
    print(i, '-', makanan, 'harganya :', harga)
print('=' * 101)

# Melooping dectiniory
data_lengkap = {'Nama': 'Danang Haris Setiawan', 'Nomor': 628817043533,
                'Agama': 'Islam', 'Pekerjaan': 'Mahasiswa', 'Hobi': 'Coding', 'Alamat': 'Tambakboyo'}


for i, data in data_lengkap.items():
    print(i, '=', data)
