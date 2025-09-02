# episode latihan logika dan komparasi
# membuat gabungan area rentang dari angka

inputUser = float(input("masukan angka kurang dari 3 atau lebih besar dari 10 :"))

# +++3----
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 :", isKurangDari)

# ---10++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Kurang dari 10 :", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print('angka yang anda masukan: ', isCorrect)