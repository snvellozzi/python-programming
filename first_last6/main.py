# Returns true if 6 is the first or last element in list
def first_last6(nums):
    if nums[0] == 6 or nums[len(nums) - 1] == 6:
        return True
    return False


print(first_last6([1, 2, 6]))
print(first_last6([6, 4, 5, 3, 2]))
print(first_last6([3, 4, 7, 8]))
print(first_last6([6, 5, 4, 6]))
