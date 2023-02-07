# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

def badMaxArea(heights):
  # patterns:
    # longest sides, meaning, the distance from one line from another
    # tallest sides,
  largest = 0

  for l in range(len(heights)):
    for r in range(l + 1, len(heights)):
      area = (r - l) * min(heights[l], heights[r])
      largest = max(area, largest)
  
  return largest

print(badMaxArea([1,8,6,2,5,4,8,3,7]))


def maxArea(heights):
  l, r = 0, len(heights) - 1
  largest = 0
  while l < r:
    area =  (r - l) * min(heights[l], heights[r])
    largest = max(area, largest)

    if heights[l] < heights[r]:
      l += 1
    else:
      r -= 1
  return largest


  
print(maxArea([1,8,6,2,5,4,8,3,7]))

# Expected output: 49