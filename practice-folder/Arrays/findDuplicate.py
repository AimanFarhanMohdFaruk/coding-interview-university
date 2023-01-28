def findDuplicate(array):
  count = {}

  for value in array:
    if value in count:
      count[value] += 1
    else:
      count[value] = 1
  for value in array:
    if count[value] > 1:
      return value
  return None

# print(findDuplicate([1,3,4,2,2]))


# def findDuplicates(array):
#   count = {}
#   duplicates = []

#   for value in array:
#     if value in count:
#       count[value] += 1
#     else:
#       count[value] = 1
#   for value in array:
#     if count[value] > 1:
#       duplicates.append(value)
#   return list(set(duplicates))

def findDuplicates(array): #works if the nums array is in the range of [1,n]
  # we know that the value of the array is from the range of [1,n]
  # Means, when we iterate through the nums - 1, we can be sure we covered the whole array
  # when iterating, we will negate the value of array[n-1] making it negative
  # when the loop meets the duplicate, it would have been marked with a negative making it less than zero
  # if it is < 0, then we append it to the duplicates array and return it.
  duplicates = []
  for num in array:
    n = abs(num) # first loop, get the value 3
    if array[n - 1] < 0: # its not more than 0
      duplicates.append(n)
    array[n-1] = -array[n-1] #
  return duplicates


print(findDuplicates([4,3,2,7,8,2,3,1]))


# pattern:
# for each number in array, iterate [n-1]
# check if its negative, if it isn't  
# then negate it.
# if it is, append it to duplicates array
# return duplicates