# program list buku

list_buku = []
while True:
    judul = input('masukan judul buku: ')
    penulis = input('masukan penulis: ')

    data_buku = [judul, penulis]
    list_buku.append(data_buku)
    
    for index,buku in enumerate(list_buku):
        print(f'{index}, {buku[0]}, {buku[1]}')
    
    isLanjut = input("apakah dilanjutkan?(y/n)")
    
    if isLanjut == 'n':
        break
    
print('program selesai')