from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    # initialize pointers and sum
    left, right, total = 0, 0, 0
    # initialize minimum length to be the length of the array plus 1 (invalid)
    min_len = len(nums) + 1

    # loop through the array
    while right < len(nums):
        # add current number to the sum
        total += nums[right]
        # move right pointer
        right += 1

        # check if the sum is greater than or equal to target
        while total >= target:
            # update minimum length if necessary
            min_len = min(min_len, right - left)
            # subtract left number from the sum and move left pointer
            total -= nums[left]
            left += 1

    # if minimum length is still the initialized value, there is no valid subarray
    if min_len == len(nums) + 1:
        return 0
    else:
        return min_len

print(minSubArrayLen(6, [1, 3, 2, 3, 4, 5, 2, 6]))
# 6