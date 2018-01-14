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


def add_two_bin_str(a, b: str) -> str:
    if len(a) == 0 and len(b) == 0:
        return ""

    if len(a) > len(b):
        a, b = b, a

    a_rev = list(reversed(a))
    b_rev = list(reversed(b))

    result = []
    carry_over = 0
    for i in range(len(a)):
        ac, bc = int(a_rev[i]), int(b_rev[i])

        s = ac + bc + carry_over
        if s > 1:
            carry_over = 1
        else:
            carry_over = 0

        modded_sum = s % 2

        result.append(modded_sum)

    left_over_b_rev = b_rev[len(a):]

    for j in range(len(left_over_b_rev)):
        bc = int(left_over_b_rev[j])

        s = bc + carry_over
        if s > 1:
            carry_over = 1
        else:
            carry_over = 0

        modded_sum = s % 2

        result.append(modded_sum)

    return "".join(reversed([str(x) for x in result]))


def multiply_two_list(num1, num2: List[int]) -> List[int]:
    result = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    strip_idx = 0
    for i, x in enumerate(result):
        if x == 0:
            strip_idx += 1
        else:
            break

    result_stripped = result[strip_idx:]
    if len(result_stripped) == 0:
        result_stripped = [0]

    return result_stripped
