## teknik menduplikat list

a = ['aknaf','otong','budi','zikri']
print(a)

b = a
print(b)

# kita akan merubah dari a
# ini akan merubah kedua list
a[1] = "Michel"
b.sort()
print(a)
print(b)

# address dari kedua list
print(f'address a = {hex(id(a))}')
print(f'address b = {hex(id(b))}')

# menduplikat list dengan copy

print("membuat list c dengan a.copy")
c = a.copy()

print(f'address a = {hex(id(a))}')
print(f'address b = {hex(id(b))}')
print(f'address c = {hex(id(c))}')

print(a)
print(b)
print(c)

c[1] = 'Putra'
print(a)
print(b)
print(c)