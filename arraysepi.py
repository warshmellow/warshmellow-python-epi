from typing import List


def dutch(pivot_index: int, nums: List[int]) -> List[int]:
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


def mod_three_sort(nums: List[int]) -> List[int]:
    # init
    lowest_eq1 = -1
    lowest_eq2 = -1

    # loop
    for i in range(len(nums)):
        # assume nums[:i] is sorted
        n = nums[i]

        if n % 3 == 0:
            if lowest_eq1 == -1 and lowest_eq2 > -1:
                # [0 0 2]
                nums[lowest_eq2], nums[i] = nums[i], nums[lowest_eq2]
                lowest_eq2 += 1
            elif lowest_eq1 > -1 and lowest_eq2 == -1:
                # [0 1 1]
                nums[lowest_eq1], nums[i] = nums[i], nums[lowest_eq1]
                lowest_eq1 += 1
            elif lowest_eq1 > -1 and lowest_eq2 > -1:
                # [0 1 1 2]
                nums[lowest_eq1], nums[i] = nums[i], nums[lowest_eq1]
                lowest_eq1 += 1
                nums[lowest_eq2], nums[i] = nums[i], nums[lowest_eq2]
                lowest_eq2 += 1

        elif n % 3 == 1:
            # [0 0]
            if lowest_eq1 == -1 and lowest_eq2 == -1:
                lowest_eq1 = i
            elif lowest_eq1 > -1 and lowest_eq2 == -1:
                # [0 1]
                pass
            elif lowest_eq1 > -1 and lowest_eq2 > -1:
                # [1 2]
                nums[lowest_eq2], nums[i] = nums[i], nums[lowest_eq2]
                lowest_eq2 += 1
            elif lowest_eq1 == -1 and lowest_eq2 > -1:
                # [2]
                nums[lowest_eq2], nums[i] = nums[i], nums[lowest_eq2]
                lowest_eq1 = lowest_eq2
                lowest_eq2 += 1

        else:
            if lowest_eq2 == -1:
                lowest_eq2 = i

    return nums


def mod_two_stable_sort(nums: List[int]) -> List[int]:
    lowest_eq1 = -1

    for i in range(len(nums)):
        n = nums[i]
        # [1, 3, 5, 0, 0] ->
        if n % 2 == 0:
            if lowest_eq1 > -1:
                for j in range(i, lowest_eq1, -1):
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                lowest_eq1 += 1
        else:
            if lowest_eq1 == -1:
                lowest_eq1 = i

    return nums
