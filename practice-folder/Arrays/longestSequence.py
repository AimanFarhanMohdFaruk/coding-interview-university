def longestSequence(array):
  numbers = set(array)
  length = 0
  for num in numbers:
      tmp = 1
      while num+1 in numbers:
          tmp += 1
          num += 1
      length = max(length,tmp)
  return length


def longestSequenceTwo(array):
  nums = set(array)
  longest = 0

  for num in nums:
    if (num - 1) not in nums: #dont check if its not the start of a sequence
      length = 1
    while (num + length) in nums: #basic increment, both to get the following number and the current length of sequence
      length += 1
      longest = max(longest, length)
  return longest
      

print(longestSequence([1,2,3,100,200]))

print(longestSequenceTwo([1,2,3,4,100, 101, 102,103,104,105,200]))

# pointers
# What makes a sequence?
  # it has a start and end,
  # the start value does not have a left neighbour

# using this logic
# we can deduce using the following:
  # for each number in the array
    # check if it has a left neighbour
      # if it doesnt, means its the start of a sequence
      # initiate the lenght of 1
      # while it has a right neighbour (num + length) that is in the array of numbers, increase the length
      # longest = max(length(which is the current running count), longest)
  # return longest