# Write a program that takes an array A and an index into A, and 
# rearranges the elements such that all elements less than A[r]
# (the "pivot") appear first, followed by elements equal to the pivot,
# followed by elements greater than the pivot.

def dutchFlagPartition(pivot_idx, arr):
  pivot = arr[pivot_idx]
  smaller = 0

  for i in range(len(arr)):
    if arr[i] < pivot:
      arr[i], arr[smaller] = arr[smaller], arr[i]
      smaller += 1
    
  larger = len(arr) - 1
  for i in reversed(range(len(arr))):
    if arr[i] < pivot:
      break
    elif arr[i] > pivot:
      arr[i] , arr[larger] = arr[larger], arr[i]
      larger -= 1
  return arr

print(dutchFlagPartition(1, [-3,0,-1,1,1,4,2]))


def dutchFlagPartitionTwo(pivot_index, A):
  pivot = A[pivot_index]

  smaller , equal, larger = 0, 0, len(A)
  while equal < larger:
    if A[equal] < pivot:
      A[smaller], A[equal] = A[equal], A[smaller]
      smaller, equal = smaller + 1, equal + 1
    elif A[equal] == pivot:
      equal += 1
    else:
      larger -= 1
      A[equal], A[larger] = A[larger], A[equal]
  return A


print(dutchFlagPartitionTwo(1, [-3,0,-1,1,1,4,2]))
