import os

def total(subtotals):
    total = 0
    for item in subtotals:
        total += item
    return total

def diskon(harga, disc):
    return harga * (disc / 100)

def subtotal(harga, discount, qty):
    return (harga - discount) * qty

data = []
while True:
    print("=" * 40)
    print(f"{'Input Data':^40}")
    print("=" * 40)
    nama = input(f"Nama Barang\t : ")
    qty = int(input(f"QTY\t\t : "))
    satuan = input(f"Satuan\t\t : ")
    ed = input(f"ED\t\t : ")
    harga = int(input(f"Harga\t\t : "))
    disc = int(input(f"Diskon %\t : "))
    os.system('cls')

    discount = diskon(harga, disc)
    subtotall = subtotal(harga, discount, qty)

    masukan = [nama, qty, satuan, ed, harga, disc, subtotall]
    data.append(masukan)

    print("=" * 98)
    print(f"{'Rincian':^98}")
    print("=" * 98)
    print(f"No | {'Nama Barang':^20} | {'QTY':^5} | {'Satuan':^10} | {'ED':^10} | {'Harga':^10} | {'Disc %':^7} | {'Subtotal':^10}")
    print("-" * 98)

    subtotals = []
    for index, item in enumerate(data):
        print(f"{index+1:>2} | {item[0]:^20} | {item[1]:^5} | {item[2]:^10} | {item[3]:^10} | {item[4]:^10,.2f} | {item[5]:^7} | {item[6]:^10,.2f}")
        subtotals.append(item[6]) 
    print("-" * 98)

    totall = total(subtotals)
    print(f"{'Total Harga':>83}: {totall:,.2f}")
    print("=" * 98)

    lanjut = input("Apakah Anda ingin memasukkan data lagi? (y/n): ").lower()
    if lanjut == 'n':
        break