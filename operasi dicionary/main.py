# operasi dictionary

data_dict = {
    'cup': 'ucup sarucup',
    'amd': 'ahmad telkomsel',
    'ynt': 'yanto radiasi'
}

# panjang dictionary
LENDICT = len(data_dict)
print(f'panjang dict = {LENDICT}')

# mengecek key exist atau tidak
KEY = 'cup'
CHECKKEY = KEY in data_dict
print(f'apakah {KEY} ada di data dict: {CHECKKEY}')

# mengakses value (read) dengan get
print(data_dict['cup'])
print(data_dict.get('cup'))

# mengupdate data
data_dict['cup'] = 'ucup batagor'
print(data_dict)
data_dict.update({'cup':'ucup handuk'})
print(data_dict)

# menambah data
data_dict['asp'] = 'asep cumi cumi'
print(data_dict)
data_dict.update({'ptr':'putra mbut'})
print(data_dict)

# mendelete data
del data_dict['ptr']
print(data_dict)