from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [2, 3, 1, 1, 4]
        last_position = len(nums) - 1

        for i in range(len(nums) -2, -1, -1):
            if i + nums[i] >= last_position:
                last_position = i
        return last_position == 0

print(Solution.canJump(0, [2, 3, 1, 1, 4]))