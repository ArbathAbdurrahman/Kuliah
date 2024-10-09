import os
import matplotlib.pyplot as plt

def rata(jumlah, total):
    return jumlah / total

def lol(poin):
    hasil = 0
    for i in poin:
        hasil += i
    return hasil

nama1 = input("Masukkan nama 1 : ")
nama2 = input("Masukkan nama 2 : ")

hitung = []
while True:
    print("="*40)
    print(f"{'Input Data':^40}")
    print("="*40)
    nama = input(f"{nama1}\t\t : ")
    keterangan = input(f"{nama2}\t\t : ")
    os.system('cls')

    data = [nama, keterangan]
    hitung.append(data)

    poin1 = []
    poin2 = []
    for i in hitung:
        poin1.append(int(i[0]))
    for i in hitung:
        poin2.append(int(i[1]))

    hasil1 = lol(poin1)
    total1 = len(poin1)
    hasil2 = lol(poin2)
    total2 = len(poin2)

    print("="*40)
    print(f"{'Hasil Pengujian':^40}")
    print("="*40)
    print(f"No | {nama1:^20} | {nama2:^15}")
    print("-"*40)
    for index, invut in enumerate(hitung):
        print(f" {index+1} | {invut[0]:^20} | {invut[1]:^15}")
    print("-"*40)
    print(f"{nama1} Tertinggi \t\t= {max(poin1)} ms")
    print(f"{nama1} Terendah \t\t= {min(poin1)} ms")
    print(f"Rata-rata {nama1} \t\t= {rata(hasil1, total1)} ms")
    print("-"*40)
    print(f"{nama2} Tertinggi \t\t= {max(poin2)} ms")
    print(f"{nama2} Terendah \t\t= {min(poin2)} ms")
    print(f"Rata-rata {nama2} \t\t= {rata(hasil2, total2)} ms")
    
    diagram = input("Tampilkan diagram? (Y/N): ")
    if diagram.upper() == 'Y':
        # Plotting the line chart
        plt.figure(figsize=(10, 5))
        
        # Creating line charts for poin1 and poin2
        x = list(range(1, len(poin1) + 1))
        plt.plot(x, poin1, marker='o', linestyle='-', label=nama1, color='b')  # Blue line for nama1
        plt.plot(x, poin2, marker='o', linestyle='-', label=nama2, color='r')  # Red line for nama2
        
        # Adding labels and title
        plt.xlabel('Pengujian ke-')
        plt.ylabel('Waktu (ms)')
        plt.title(f'Perbandingan Data {nama1} dan {nama2}')
        plt.xticks(x)  # Setting x-ticks to show each point
        plt.legend()

        # Menampilkan nilai tertinggi, terendah, dan rata-rata di grafik
        plt.text(len(poin1), max(poin1), f'Max {nama1}: {max(poin1)}', color='blue', ha='right')
        plt.text(len(poin1), min(poin1), f'Min {nama1}: {min(poin1)}', color='blue', ha='right')
        plt.text(len(poin1), rata(hasil1, total1), f'Avg {nama1}: {rata(hasil1, total1):.2f}', color='blue', ha='right')

        plt.text(len(poin2), max(poin2), f'Max {nama2}: {max(poin2)}', color='red', ha='right')
        plt.text(len(poin2), min(poin2), f'Min {nama2}: {min(poin2)}', color='red', ha='right')
        plt.text(len(poin2), rata(hasil2, total2), f'Avg {nama2}: {rata(hasil2, total2):.2f}', color='red', ha='right')
        
        # Displaying the diagram
        plt.show()
