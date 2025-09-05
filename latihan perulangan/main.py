# latihan perulangan membuat segitiga

sisi = 10

# Menggunakan For
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
    
# Menggunakan While
count = 1
while True:
    print("*"*count)
    count += 1
    
    if count > sisi:
        break
    
# Hanya ganjil saja
print("GANJIL SAJA")
count = 1
while True:
    # akan kembali ke atas jika ganjil
    if (count%2):
        print("*"*count)
        count += 1
    else:
        count += 1
        continue
    
    # akan break jika count melebihi sisi
    if count > sisi:
        break
    
print("TENGAH")
count = 1
spasi = int(sisi/2)
while True:
    # akan kembali ke atas jika ganjil
    if (count%2):
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    
    # akan break jika count melebihi sisi
    if count > sisi:
        break