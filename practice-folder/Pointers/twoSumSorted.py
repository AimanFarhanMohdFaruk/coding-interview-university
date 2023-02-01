from typing import List
def twoSum(numbers: List[int], target: int) -> List[int]:
  l,r = 0, len(numbers) - 1

  while l < r:
    curSum = numbers[l] + numbers[r]
    
    if curSum > target:
      r -= 1
    elif curSum < target:
      l += 1
    else:
      return [l + 1, r + 1]

print("Two Sum:", twoSum([2,7,11,15], 9))

# the instructions here requires that you add one to the answers. For whatever reason.


# Instructions, find the combinations of 3 numbers that amount to zero. You cannot have duplicates in your answers
def threeSum(numbers: List[int]) -> List[int]:
  res = []
  numbers.sort()

  for i, a in enumerate(numbers):
    # SKIP the start value is the same
    if i > 0 and a == numbers[i - 1]:
      continue
    l, r = i + 1, len(numbers) - 1

    while l < r:
      threeSum = a + numbers[l] + numbers[r]
      if threeSum > 0:
        r -= 1
      elif threeSum < 0:
        l += 1
      else:
        res.append([a, numbers[l], numbers[r]])
        l += 1
        # SKIP DUPLICATE VALUE ON THE LEFT POINTER
        while numbers[l] == numbers[l - 1] and l < r:
          l += 1
  return res

print("Three sum:", threeSum([-1, 0, 1, 2, -1, -4]))
