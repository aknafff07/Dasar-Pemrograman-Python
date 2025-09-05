# nested list

data_0 = [1,2]
data_1 = [3,4]

list_biasa = [1,2,3,4]
print(list_biasa)

list_2D = [data_0,data_1]
print(f"list dua dimensi = {list_2D}")

# contoh penggunaan
peserta_0 = ['ucup', 25, 'laki-laki']
peserta_1 = ['aknaf', 19, 'laki-laki']
peserta_2 = ['michel', 10, 'perempuan']

list_peserta = [peserta_0, peserta_1, peserta_2]
print(list_peserta)

for peserta in list_peserta:
    print(f"nama : {peserta[0]}")
    print(f"umur : {peserta[1]}")
    print(f"gender : {peserta[2]}")
    
# dengan reference
list_copy = list_peserta.copy()
print(f'peserta = {list_copy}')
peserta_0[0] = 'asep'
print(f'list peserta = {list_peserta}')