# def containsDuplicate(numsArr):
#   count = {}

#   for value in numsArr:
#     if value in count:
#       count[value] += 1
#     else:
#       count[value] = 1

#   for value in numsArr:
#     if count[value] >  1:
#       return True
#   return False

def containsDuplicate(numsArr):
  return len(numsArr) != len(set(numsArr))

# def containsDuplicate(numsArr): 
# This fails if the duplicate is on either end
#   leftIdx = 0
#   rightIdx = len(numsArr) - 1

#   while leftIdx < rightIdx:
#     if numsArr[leftIdx] == numsArr[rightIdx]:
#       return True
#     else:
#       leftIdx += 1
#       rightIdx -= 1
#   return False

print(containsDuplicate([4,3,4,1]))
