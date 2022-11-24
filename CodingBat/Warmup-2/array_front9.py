# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

def array_front9(nums):
    ultimo = len(nums)
    if ultimo > 4:
        ultimo = 4

    for numero in range(ultimo):
        if nums[numero] == 9:
            return True

    return False