# List

# kumpulan data numbers
data_angka = [1,5,3,2,3]
print(data_angka)

# kumpulan data string
data_string = ['aknaf','otong','ucup']
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# kumpulan campuran
data_campuran = [1,'aknaf',True]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10,2)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop
data_list_for = [i**2 for i in range(0,10)]
print(data_list_for)

# membuat list pake for pake if
pake_for_if = [i for i in range(0,10) if i != 5]
print(pake_for_if)