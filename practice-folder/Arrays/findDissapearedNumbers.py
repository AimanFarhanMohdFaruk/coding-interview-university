def findDissapearedNumbers(nums):
  return list(set(range(1, len(nums) + 1)) - set(nums))

print(findDissapearedNumbers([1,2,3,6,5,6,7]))