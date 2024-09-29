JADWAL = {
    'SENIN': {
        'Sistem Operasi': [(15.25, 17.15), {'FST': 103}],
    },
    'SELASA': {
        'Keamanan Komputer': [(7.00, 8.45), {'FST': 407}],
        'Sistem Operasi': [(9.45, 11.30), {'FST': 302}],
        'Bahasa-bahasa Pemrograman': [(16.25, 18.05), {'FST': 303}],
    },
    'RABU': {
        'Teori Bahasa dan Otomata': [(7.00, 8.35), {'FST': 407}],
        'Komputasi Paralel': [(8.50, 10.35), {'FST': 407}],
    },
    'KAMIS': {
        'Konsep Bahasa Pemrograman': [(7.00, 8.45), {'FST': 305}],
        'Kecerdasan Buatan': [(10.40, 12.20), {'FST': 401}],
        'Analisis Algoritma dan Struktur Data': [(15.30, 17.15), {'FST': 402}],
    },
    "JUM'AT": {
        'Analisis Algoritma dan Struktur Data': [(7.00, 8.45), {'FST': 407}],
        'Bahasa-bahasa Pemrograman': [(8.50, 10.35), {'FST': 407}],
    },
}






import os
while True :
    Hari = input('Masukkan hari: ').upper()
    if Hari in JADWAL:
        os.system('cls')
        for key, value in JADWAL[Hari].items():
            print(f"{Hari} \t : {key}")

            tuple_value = value[0]
            if tuple_value:
                gabung = " - ".join([f"{jam:.2f}" for jam in tuple_value])
                print(f"Jam \t : {gabung}")
            
            dict_value = value[1]
            if dict_value:
                for sub_key, sub_value in dict_value.items():
                    print(f"{sub_key}\t : {sub_value}\n")
    else:
        print('Hari tidak ditemukan dalam jadwal.')
