# def validateSubsequence(firstArr, secArr):

#   arrayCount = 0
#   for num in firstArr:
#     if num in secArr:
#       arrayCount += 1
#     if arrayCount == len(secArr):
#       return True
#   return False

# print(validateSubsequence([5,1,22,25,6], [1,25,6]))
 # fails with duplicates


def validateSubsequenceTwo(array, sequence):
  arrIdx = 0
  seqIdx = 0
  while arrIdx < len(array) and seqIdx < len(sequence):
    if array[arrIdx] == sequence[seqIdx]:
      seqIdx += 1
    arrIdx += 1
  return seqIdx == len(sequence)


print(validateSubsequenceTwo([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 25, 22, 6, -1, 8, 10]))


def isValidSub(array, sequence):
  seqIdx = 0
  for value in array:
    if seqIdx == len(sequence):
      break
    if sequence[seqIdx] == value:
      seqIdx += 1
  return seqIdx == len(sequence)

print(isValidSub([5,1,22,25,6], [1,25,6]))
