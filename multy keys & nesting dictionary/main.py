import datetime

mahasiswa = {
    'nama': 'akanf saputra',
    'nim': '415240',
    'sks_lulus': 140,
    'beasiswa': True,
    'lahir': datetime.datetime(2006,2,12)
}

mahasiswa2 = {
    'nama': 'ucup batagor',
    'nim': '415240',
    'sks_lulus': 140,
    'beasiswa': False,
    'lahir': datetime.datetime(2003,2,25)
}

mahasiswa3 = {
    'nama': 'otong mbut',
    'nim': '415240',
    'sks_lulus': 140,
    'beasiswa': True,
    'lahir': datetime.datetime(2000,4,12)
}

data_mahasiswa = {
    'MAH001': mahasiswa,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3
}

print(f'{'KEY':<7} {'Nama':<17} {'NIM':<6} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}')
print('-'*60)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    
    print(f'{KEY:<7} {NAMA:<17} {NIM:<6} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}')