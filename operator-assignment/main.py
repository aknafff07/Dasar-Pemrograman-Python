# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5 # ini adalah assignment
print(a)

a += 1 # artinya a = a + 1
print('nilai a: ',a)

a -= 2 # artinya a = a - 2
print('nilai a: ',a)

a *= 5 # artinya a = a * 5
print('nilai a: ',a)

a /= 2 # artinya a = a / 2
print('nilai a: ',a)

b = 10
print('nilai b:', b)

# modulus dana floor division
b %= 3
print('nilai b: ',b)

b //= 3
print('nilai b: ',b)

# pangkat atau eksponen
a = 5
print('nilai a: ',a)
a **= 3
print('nilai a: ',a)

# operasi bitwise
# OR
c = True
print('nilai c =', c)
c |= False
print('nilai c =', c)

c = False
print('nilai c =', c)
c |= False
print('nilai c =', c)

# AND
c = True
print('nilai c =', c)
c &= False
print('nilai c =', c)

c = True
print('nilai c =', c)
c &= True
print('nilai c =', c)

# XOR
c = True
print('nilai c =', c)
c ^= False
print('nilai c =', c)

c = False
print('nilai c =', c)
c ^= False
print('nilai c =', c)

# geser-geser
d = 0b0100
print('nilai d:', format(d, '04b'))
d >>= 2
print('nilai d:', format(d, '04b'))
d <<= 2
print('nilai d:', format(d, '04b'))