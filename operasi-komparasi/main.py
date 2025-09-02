# operasi komparasi
# setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
hasil = a > 3
print('hasilnya: ',hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)

# kurang dari <
print("====KURANG DARI====")
hasil = b < 3
print(b, '<', 3, '=', hasil)

# lebih dari sama dengan >=
print("====LEBIH DARI SAMADENGAN====")
hasil = b >= 3
print(b, '>=', 3, '=', hasil)

# kurang dari sama dengan <=
print("====KURANG DARI SAMADENGAN====")
hasil = b <= 3
print(b, '<=', 3, '=', hasil)

# sama dengan sama dengan ==
print("====SAMADENGAN SAMADENGAN====")
hasil = b == 3
print(b, '==', 3, '=', hasil)

# tidak sama dengan >=
print("====TIDAK SAMADENGAN====")
hasil = b != 3
print(b, '!=', 3, '=', hasil)

# 'is' sebagai komparasi objek identity
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x=', x, ',id =', hex(id(x)))
hasil = x is y
print('x is y =', hasil)

# 'is not' sebagai komparasi objek identity
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x=', x, ',id =', hex(id(x)))
hasil = x is not y
print('x is not y =', hasil)