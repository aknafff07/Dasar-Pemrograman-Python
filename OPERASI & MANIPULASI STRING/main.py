# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = 'ucup'
nama_kedua = 'syahroni'
nama_akhir = 'ahmad'

nama_lengkap = nama_pertama + ' ' + nama_kedua + ' ' + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang dari string
panjang = len(nama_lengkap)
print(str(panjang))

# 3. operator untuk string
# mengecek apakah ada komponen char atau string di string
d = 'z'
status = d in nama_lengkap
print(status)

d = 'z'
status = d not in nama_lengkap
print(status)

# mengulang string
print("syahroni"*3)

# indexing
print('index ke-0 :', nama_lengkap[5])
print('index ke-(-1) :', nama_lengkap[-1])
print('index ke-[0:3]:', nama_lengkap[0:3])
print('index ke-[0,2,4,6]:', nama_lengkap[0:10:2])

# item paling kecil
print('paling kecil: ', min(nama_lengkap))
# item paling besar
print('paling besar: ', max(nama_lengkap))

ascii_code = ord(" ")
print("ascii code spasi adalah ", str(ascii_code))

# 4. operator dalam bentuk method
data = "otong surotong syahroni"
jumlah = data.count("o")
print('jumlah o: ', str(jumlah))