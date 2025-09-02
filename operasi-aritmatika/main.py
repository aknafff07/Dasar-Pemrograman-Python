# operasi aritmatika

a = 10
b = 5

# Operasi tambah +
hasil = a + b
print(a, '+', b, '=', hasil)

# Operasi kurang -
hasil = a - b
print(a, '-', b, '=', hasil)

# Operasi kali *
hasil = a * b
print(a, '*', b, '=', hasil)

# Operasi bagi /
hasil = a / b
print(a, '/', b, '=', hasil)

# Operasi eksponen(pangkat) **
hasil = a ** b
print(a, '**', b, '=', hasil)

# Operasi modulus(sisa bagi) %
hasil = a % b
print(a, '%', b, '=', hasil)

# Operasi floor division(kebalikan modulus) //
hasil = a // b
print(a, '//', b, '=', hasil)

# prioritas operasi, opearional precedence
x = 3
y = 2
z = 4

hasil1 = x ** y * z + x / y - y % z // x
print("hasilnya =", hasil1)