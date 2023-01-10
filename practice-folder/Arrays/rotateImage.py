def rotateImage(array):
  l = 0
  r = len(array) - 1

  while l < r:
    array[l], array[r] = array[r], array[l]
    l += 1
    r -= 1
  for i in range(len(array)):
    for j in range(i):
      array[i][j], array[j][i] = array[j][i] , array[i][j]
  return array

print(rotateImage([[1,2,3],[4,5,6],[7,8,9]]))