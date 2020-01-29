# Dictionary : tipe data associstive
# var = {key:values}
print("=" * 100)

member1 = {"ID": 101, "Nama": "Danang Haris Setiawan",
           "Pekerjaan": "Mahasiswa", "Status Member": "Gold"}
member2 = {"ID": 102, "Nama": "Sandika Galih",
           "Pekerjaan": "Dosen", "Status Member": "Berlian"}

print(member1.keys())
print(member2.values())
print(member1.items())
print(member1.get("ID"))
print("=" * 100)

memberList = member1, member2
member = {101: member1, 102: member2}

print(member1["ID"])
print(memberList[0]["Nama"])
print("=" * 100)

print(member[101])
print(member[101]["Nama"])
print(member[102]["Pekerjaan"])
print(member.keys())
