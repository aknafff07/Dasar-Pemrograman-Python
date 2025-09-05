## Operasi

data = ['aknaf','putra','ucup']

# mengambil data dari list ini
data_0 = data[0]
print(data_0)

data_terakhir = data[-1]
print(data_terakhir)

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data {panjang_data}")

## manipulasi list
# menambahkan item pada list sesuai posisi
print(f"data sebelum di ubah = {data}")

data.insert(1, "Otong")
print(f"data sesudah di tambah = {data}")

# menambah di akhir list
data.append("budi")
print(data)

# menambah list dengan list
data_baru = ['anto','yanto']
data.extend(data_baru)
print(f"data gabungan = {data}")

# merubah data
# kita ubah data 2 menjadi michel
data[2] = "Michel"
print(f'data setelah dirubah = {data}')

# meremove data
data.remove('Otong')
print(data)

# meremove data paling belakang
data.pop()
print(data)