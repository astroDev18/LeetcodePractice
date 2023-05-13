from typing import List

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 3 values - reach = max reachable length
        # count = number of jumps
        # last = right most index reached
        reach, count, last = 0, 0, 0
        # loop through array excluding last element
        for i in range(len(nums)-1):
            # update reach to the max value reachable
                reach = max(reach, i + nums[i])
            # if i has reached the last index reachable
                if i == last:
                # update last reachable value
                    last = reach
                # increase number of jumps made
                    count += 1
        return count

print(Solution.jump(0, [2, 3, 1, 1, 4]))
