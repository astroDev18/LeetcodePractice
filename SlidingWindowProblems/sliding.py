# Write an algorithm to return the shortest length that totals to target
# [1, 3, 2, 3, 4, 5, 2, 6] Target = 6
from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
# init 3 variables, right, left, and total
    right, left, total = 0, 0, 0
# init min_length to store the min length. Set to len + 1
    min_len = len(nums) + 1
# While loop for when right < len(nums):
    while right > len(nums):
# add right value to total
        total += nums[right]
# increment one to right
        right += 1
# While loop for total >= target
        while total >= target:
# check if min_length is changed compared to current min_length
            min_len = min(min_len, right-left)
# increment left by 1
            left += 1
# subtract total by left (sliding window)
            total -= nums[left]
# check if min_length is equal to len(nums) + 1
    if min_len == len(nums) + 1:
        return 0
# return answer if no
    else:
        return min_len

print(minSubArrayLen(6, [1, 3, 2, 3, 4, 5, 2, 6]))