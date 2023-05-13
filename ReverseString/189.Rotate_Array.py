from typing import List


class Solution:
    def reverse(self, nums, i, j):
        left = i
        right = j
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k < 0:
            k += len(nums)

        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

print(Solution.rotate(0, [1,2,3,4,5,6,7], 3))