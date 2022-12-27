# def TwoNumberSum(array, targetSum):
#   for i in range(len(array) - 1):
#     firstNum = array[i]
#     for j in range(i + 1, len(array)):
#       secondNum = array[j]
#       if firstNum + secondNum == targetSum:
#         return [firstNum , secondNum]
#   return []

def TwoNumberSum(array, targetSum):
  nums = {}
  for num in array:
    potentialMatch = targetSum - num
    if potentialMatch in nums:
      return [potentialMatch, num]
    else:
      nums[num] = True
  return []

print(TwoNumberSum([1,3,4,-9], 7))

def twoNumberSumThree(array, targetSum):
  array.sort()
  left = 0
  right = len(array) - 1
  while left < right:
    currentSum = array[left] + array[right]
    if currentSum == targetSum:
      return [array[left], array[right]]
    elif currentSum < targetSum:
      left += 1
    elif currentSum > targetSum:
      right -= 1
  return []

print(twoNumberSumThree([1,3,4,-9], 7))

## What's the tradeoff and techniques used ?
# The first one runs in linear time since we iterate through once.
# The second one runs in O(log n) since 
