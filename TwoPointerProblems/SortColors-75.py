# Given an array nums, return the sorted array.
# Only Integers 0, 1, and 2 will be used
# nums = [2,0,2,1,1,0]
# output = [0,0,1,1,2,2]
from typing import List

class Solution:
    def sortColors(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left starts at beginning, i starts at beginning, right starts at end
        l, i, r = 0, 0, len(nums) - 1
        # create function to swap values
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        # loop until i meets right, which we know means all values are sorted
        while i <= r:
            # if it is 0 swap with 1, and move left forward since we know the preceding value is 0
            if nums[i] == 0:
                swap(l, i)
                l += 1
            # If num is 2, swap with i. Move right 1 forward since we know right is 2
            elif nums[i] == 2:
                swap(r, i)
                r -= 1
                i -= 1
            # increment i by 1
            i += 1


