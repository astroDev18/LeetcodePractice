from typing import List


# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i].
# Input: nums = [1,2,3,4] Output: [24,12,8,6]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create an empty array filled with 1's
        res = [1] * len(nums)
        prefix = 1
        postfix = 1
        # iterate over nums
        for i in range(len(nums)):
            # fill res values with prefix
            res[i] = prefix
            # modify prefix in place
            prefix *= nums[i]
        # do reverse for postfix
        for i in range(len(nums) - 1, -1, -1):
            # modify postfix in place
            res[i] *= postfix
            # update postfix value
            postfix *= nums[i]
        return res

print(Solution.productExceptSelf(0, [1,2,3,4]))

tests = [
    (
        ([1, 2, 3, 4],),
        ([24, 12, 8, 6])
    ),
    (
        ([-1,1,0,-3,3],),
        ([0,0,9,0,0])
    )
]

