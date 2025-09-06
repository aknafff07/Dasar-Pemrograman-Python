# looping dari list

# for loop
kumpulan_angka = [4,3,2,4,5,4,3,2,5]

for angka in kumpulan_angka:
    print(f'angka = {angka}')
    
peserta = ['ucup','aknaf','otong']

for nama in peserta:
    print(f'nama = {nama}')
    
# for loop dan range
kumpulan_angka = [10,9,7,1,8]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f'angka = {kumpulan_angka[i]}')
    
# while
kumpulan_angka = [10,9,7,1,8]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f'angka = {kumpulan_angka[i]}')
    i += 1
    
# list comprehension
data = ['aknaf',1,2,3,'otong']

[print(f'data = {i}') for i in data]

# enumerate
data = ['aknaf',1,2,3,'otong']

for index,data in enumerate(data):
    print(f'index = {index}, data = {data}')
