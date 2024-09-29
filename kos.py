kos = {
    'kamar1' : None,
    'kamar2' : None,
    'kamar3' : None,
    'kamar4' : None,
    'kamar5' : None,
}

def new(penghuni,kamar):
    for kamar, penghuni_kamar in kos.items():
        if penghuni_kamar is None:
            kos[kamar] = penghuni
            print(f'Penghuni "{penghuni}" telah ditambahkan ke {id(kamar)}.')
            return
    print('Semua kamar sudah penuh')
while True :
    baru = input('masukan penghuni : ')
    new(baru,kos) 
    print(kos)