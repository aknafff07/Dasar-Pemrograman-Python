# operator dalam bentuk methods
## merubah case dari string

# merubah semua ke uppercase
salam = "haii"
print(salam)
salam = salam.upper()
print('upper:', salam)

# merubah semua ke lowercase
alay = "AKNAF SAPUTRA"
print(alay)
alay = alay.lower()
print('lower:', alay)

## pengecekan dengan isX method
# contoh untuk pengecekan lower case
salam = 'SIS'
apakah_lower = salam.islower()
print(str(apakah_lower))
apakah_upper = salam.isupper()
print(str(apakah_upper))

#isalpha() adalah untuk mengecek apakah semuanya huruf
#isalnum() adalah huruf dan angka
#isdecimal() adalah untuk angka saja
#isspace() adalah spasi, tab, newline (\n)
#istitle() adalah semua kata dimulai dengan huruf besar

judul = "Belajar Python Pemula"
cek_judul = judul.istitle()
print(cek_judul)

## ngecek komponen startswith() endswith()
cek_start = "Aknaf Saputra".startswith("Aknaf")
print(cek_start)

cek_end = "Aknaf Saputra".endswith("Saputra")

## penggabungan komponen join() split()
pisah = ['aknaf','saputra']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = "akusnjsaputra"
print(gabungan.split('snj'))

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10,"-")
print("'", tengah, "'")

# kebalikannya strip()
tengah = tengah.strip("-")
print("'", tengah, "'")