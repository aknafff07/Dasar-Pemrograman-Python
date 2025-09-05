data_angka = [1,2,5,3,6,4,6,7]

print(f"data angka = {data_angka}")

# count data
jumlah_data_6 = data_angka.count(6)
jumlah_data_2 = data_angka.count(2)

print(jumlah_data_6)
print(jumlah_data_2)

# ambil posisi data
data = ['aknaf','ucup','otong','budi']
print(data)

index_ucup = data.index("ucup")
print(f'index si ucup = {index_ucup}')

# mengurutkan list
print(f'data angka sebelum di sort = {data_angka}')
data_angka.sort()
print(f'data angka sort = {data_angka}')

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f'data angka reverse = {data_angka}')
print(f'data reverse = {data}')