# copy dictionary

teman_teman = {
    'cup': 'ucup somay',
    'tong': 'otong galon',
    'ahm': 'ahmad telkomsel',
    'ynt': 'yanto deterjen'
}

friends = teman_teman.copy()
print(f'teman-teman : {teman_teman}')
print(f'friends: {friends}')

teman_teman['cup'] = 'ucup batagor'
print(f'teman-teman : {teman_teman}')
print(f'friends: {friends}')

# pop dictionary (berdasarkan key)
data_ucup = friends.pop('cup')
print(f'data ucup = {data_ucup}')
print(f'friends = {friends}')

# pop item dictionary (yang terakhir aja)
data_last = friends.popitem()
print(f'data terakhir = {data_last}')
print(f'friends = {friends}')