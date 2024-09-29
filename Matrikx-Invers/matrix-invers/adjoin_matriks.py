
def adjoin(matrix):
  output = [[0,0] , [0,0]]
  if len(matrix) < 2:
    return None
  output[0][0] = matrix[1][1]
  output[0][1] = -matrix[0][1]
  output[1][0] = -matrix[1][0]
  output[1][1] = matrix[0][0]
  return output
  