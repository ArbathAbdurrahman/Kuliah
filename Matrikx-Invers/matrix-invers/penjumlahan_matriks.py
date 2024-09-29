def penjumlahan_matriks(matriks1 , matriks2):
  if len(matriks1) < 2 or len(matriks2) < 2:
    return None
  output = [[0,0] , [0,0]]
  output[0][0] = matriks1[0][0] + matriks2[0][0]
  output[0][1] = matriks1[0][1] + matriks2[0][1]
  output[1][0] = matriks1[1][0] + matriks2[1][0]
  output[1][1] = matriks1[1][1] + matriks2[1][1]
  return output
