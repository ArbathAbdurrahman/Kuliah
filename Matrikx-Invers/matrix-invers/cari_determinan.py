def cari_determinan(matrix):
  if len(matrix) < 2:
    print "jjjj"
    # Untuk mengatasi error jika matriks kurang dari 2 kolom maka return None
    return None 
  a, b = matrix[0][0], matrix[0][1]
  c, d = matrix[1][0], matrix[1][1]

  determinan = a*d - b*c
  
  return determinan


