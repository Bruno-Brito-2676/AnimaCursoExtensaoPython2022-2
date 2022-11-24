#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  for numero in range(len(nums)-2):
    if nums[numero] == 1 and nums[numero+1] == 2 and nums[numero+2] == 3:
      return True
  return False