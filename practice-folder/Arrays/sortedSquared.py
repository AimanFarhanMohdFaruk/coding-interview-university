def sortedSquares(array):
  squared = []
  for value in array:
    product = value * value
    squared.append(product)
  
  squared.sort()
  return squared

print(sortedSquares([1,2,3,5]))


# Tips, we can initialise an arrays of zero
# using, [0 for _ in array]

def sortedSquaresTwo(array):
  sortedSquares = [0 for _ in array]

  for i in range(len(array)):
    value = array[i]
    sortedSquares[i] = value * value

  sortedSquares.sort()
  return sortedSquares