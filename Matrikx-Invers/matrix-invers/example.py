from cari_determinan import cari_determinan
# from lihat_matriks import lihat
from penjumlahan_matriks import penjumlahan_matriks
from invers_determinan import invers_det
from cek_determinan import cek_determinan
from adjoin_matriks import adjoin
#import yang dibutuhkan dapat diimport seperlunya

#Ini adalah file contoh penggunaan library

#1. Determinan matriks
matriks1 = [[1,2] , [3,4]]
matriks2 = [[5,6] , [7,8]]
hasil_determinan1 = cari_determinan(matriks1) #hasil determinan untuk matriks 1
hasil_determinan2 = cari_determinan(matriks2)
#hasil determinan untuk matriks 2

print("Hasil determinan dari matriks 1 :" , hasil_determinan1)
print("Hasil determinan dari matriks 2 :" , hasil_determinan2)

# 2. Cek determinan
#Output berupa boolean
print(cek_determinan(matriks1)) 
print(cek_determinan(matriks2))

# 3. Adjoin matriks
print(adjoin(matriks1))
print(adjoin(matriks2))


# 4. Nilai invers determinan
invers_determinan1 = invers_det(hasil_determinan1)
invers_determinan2 = invers_det(hasil_determinan2)