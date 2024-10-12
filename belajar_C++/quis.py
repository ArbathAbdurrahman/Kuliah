def basis(x,y):
    hasil = 1
    for _ in range(y):
        hasil *= x
    return hasil

while True :
    x = int(input("Masukan angka : "))
    y = int(input("Masukan pangkat : "))
    print(basis(x,y))