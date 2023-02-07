# Problem

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

from typing import List

def trapWater(height: List[int]) -> int:

  if not height: return 0

  l , r = 0 , len(height) - 1
  leftMax, rightMax = height[l] , height[r]
  res = 0
  while l < r:
    if leftMax < rightMax:
      l += 1
      leftMax = max(leftMax, height[l]) # having this step allows you to avoid getting a negative numb
      res += leftMax - height[l]
    else:
      r -= 1
      rightMax = max(rightMax, height[r])
      res += rightMax - height[r]

  return res

print(trapWater([0,1,0,2,1,0,1,3,2,1,2,1]))