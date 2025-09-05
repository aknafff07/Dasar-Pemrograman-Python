data_0 = [1,2]
data_1 = [4,5]

data_2D = [data_0,data_1]
data_2D_copy = data_2D.copy()
print(data_2D)
print(f'data 2d copy = {data_2D_copy}')

# mengambil data
data = data_2D[0][1]
print(data)

# address semuanya
print(f'address data 2d asli = {hex(id(data_2D))}')
print(f'address data 2d copy = {hex(id(data_2D_copy))}')

print(f'address dari member ke 1')
print(f'address data 2d asli = {hex(id(data_2D[0]))}')
print(f'address data 2d copy = {hex(id(data_2D_copy[0]))}')

# kita gunakan deep copy
from copy import deepcopy

data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)
print(f'address data 2d asli = {hex(id(data_2D))}')
print(f'address data 2d copy = {hex(id(data_2D_deepcopy))}')

print(f'address dari member ke 1')
print(f'address data 2d asli = {hex(id(data_2D[0]))}')
print(f'address data 2d copy = {hex(id(data_2D_deepcopy[0]))}')

data_2D[1][0] = 30
print(data_2D)
print(f'data 2d copy = {data_2D_copy}')
print(f'data 2d deepcopy = {data_2D_deepcopy}')