# continue dan pass

# pass -> dia berfungsi sebagai dummy, tidak akan di eksekusi
angka = 0

while angka < 5:
    angka += 1
    
    if angka == 3:
        pass # tidak akan di eksekusi
    
    print(angka)

print("akhir program")

# continue
angka2 = 0

while angka2 < 5:
    angka2 += 1
    print(f"angka sekarang -> {angka2}")
    
    if angka2 == 3:
        print("disini angka 3")
        continue # akan membuat loop meloncat ke step selanjutnya
    
    print("yoooooooo")
    
print("akhir program")