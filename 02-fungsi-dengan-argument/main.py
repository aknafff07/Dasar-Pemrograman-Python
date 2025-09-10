# fungsi dengan argument

# def nama_fungsi(parameter/argument/input):
#     #badan fungsi

def hello_world(nama):
    # fungsi hello world menerima input dengan variabel nama
    print(f'selamat datang {nama}')

hello_world('aknaf')
hello_world('saputra')

# program tambah
def tambah(angka_1, angka_2):
    # fungsi tambah
    hasil = angka_1 + angka_2
    print(f'{angka_1} + {angka_2} = {hasil}')
    
tambah(1, 7)
tambah(2, 5)

def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f'yang terhormat {peserta}')

anggota = ['aknaf','otong','yanto']

say_hi(anggota)