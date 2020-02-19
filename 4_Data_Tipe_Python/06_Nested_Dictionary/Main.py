'''
Nested Dictionary adalah: dictionary di dalam dictionary, kumpulan dectionari di dalam dictionary tunggal.
nes_dict = {"dict1": {key1: val1},
            "dict2": {key2: val2}
            }
        - nes_dict adalah nested dictionary yang didalamnya terdapat 2 dictionary (dict1 & dict2)
        - dict1 & dict2 adalah dictionary yang memiliki key dan value masing-masing.
'''

# Membuat nested dictionary
orang = {
    1: {"nama": "Sherlock Holmes", "umur": "35", "kelamin": "pria"},
    2:{"nama":"Conan Doyle", "umur":"18", "kelamin":"pria"}
}

# Mengakses nested dictionary
print(orang)
print(orang[1]["nama"])
print(orang[1]["umur"])
print(orang[1]["kelamin"])

# Menambahkan element ke nasted dictionary
orang[3] = {}
orang[3]["nama"] = "Via"
orang[3]["umur"] = "17"
orang[3]["kelamin"] = "Perempuan"
orang[3]["menikah"] = "tidak"
print(orang[3])

orang[4] = {"nama": "Aisyah", "umur": "21", "kelamin": "perempuan", "menikah": "ya"}
print(orang[4])

# Menghapus elemennt dari nested dictionary
del orang[3]["menikah"]
del orang[4]["umur"]
print(orang[3])
print(orang[4])

# Menghapus dictionari dari nested dictionary
del orang[3], orang[4]
print(orang)

# Iterasi nested dictionary
for org_id,org_data in orang.items():
    print('\nOrang ID: ', org_id)
    for data in org_data:
        print(data + ':', org_data[data])

'''
Poin Penting:
1 - Nested dictionary adalah kumpulan dictionary yang tidak brtaturan.
2 - Nested dictionary tidak memungkinkan untuk di iris.
3 - Nested dictonary dapat di perkecil dan di perbesar sesuai kebutuhan.
4 - Sama seperti dictionary, nested dictionari memiliki key dan value.
5 - dictionary pada nested dictionary diakses menggunakan key.
'''