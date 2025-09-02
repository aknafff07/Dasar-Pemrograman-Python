# width and multiline

# Data
data_nama = "aknaf"
data_umur = 19
data_tinggi = 160.5
data_nomor_sepatu = 41

#string standard
data_string = f"nama {data_nama}, umur {data_umur}, tinggi {data_tinggi}, nomor sepatu {data_nomor_sepatu}"
print(data_string)

# string multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama {data_nama}, \numur {data_umur}, \ntinggi {data_tinggi}, \nnomor sepatu {data_nomor_sepatu}"
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama = {data_nama},
umur = {data_umur},
tinggi = {data_tinggi}
nomor sepatu = {data_nomor_sepatu}

"""

print(data_string)

# mengatur lebar
data_string = f"""
nama = {data_nama:>6},
umur = {data_umur:>6},
tinggi = {data_tinggi}
nomor sepatu = {data_nomor_sepatu}

"""

print(data_string)