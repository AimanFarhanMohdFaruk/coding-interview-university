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
  numbers = set(array)
  longest = 0

  for num in numbers:
    if(num - 1) not in numbers:
      length = 1
      while (num + length) in numbers:
        length += 1
      longest = max(length, longest)
  return longest

print(longestSequence([1,2,3,100,200]))

print(longestSequenceTwo([1,2,3,100,200]))