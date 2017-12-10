def sumsum(nums):
    return sum(nums)


def dutch(pivot_index, nums):
    pivot = nums[pivot_index]

    smaller = 0
    for i, _ in enumerate(nums):
        if nums[i] < pivot:
            nums[i], nums[smaller] = nums[smaller], nums[i]
            smaller += 1

    larger = len(nums) - 1
    for i in reversed(range(len(nums))):
        if nums[i] < pivot:
            break
        elif nums[i] > pivot:
            nums[i], nums[larger] = nums[larger], nums[i]
            larger -= 1

    return nums
