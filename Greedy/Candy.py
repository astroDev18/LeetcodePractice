from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Make use of two 1-d arrays, left2right and right2left
        # left2right stores number of candies required taking care of only left side
        # right2left stores number of candies required taking care of only right side
        sum = 0
        n = len(ratings)
        left2right = [1] * n
        right2left = [1] * n
        # Rule: Student with higher rating then neighbor should always get more candies

        # Traverse array left to right and whenever current elements ratings
        # is larger then the left neighbor we update the current elements candies in the left2right array
        # as left2right[i] = left2right[i-1] + 1
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left2right[i] = left2right[i-1] + 1
        # Traverse array right to left and update right2left[i]
        # right2left[i] = right2left[i+1] + 1 wherever the current ith element has higher ratings than the right i+1th element
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right2left[i] = right2left[i+1] + 1
        # for the ith student in array, we give
        # max(left2right[i], right2left[i])) in order to satisfy both left and right neighbor relationship
        for i in range(n):
            sum += max(left2right[i], right2left[i])
        return sum

# Naive Approach O(n^2) time complexity

# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         candies = [1] * len(ratings)
#         hasChanged = True
#
#         while hasChanged:
#             hasChanged = False
#             for i in range(1, len(ratings)):
#                 if i != len(ratings) and ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
#                     candies[i] = candies[i+1] + 1
#                     hasChanged = True
#
#                 if i > 0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
#                     candies[i] = candies[i-1] + 1;
#                     hasChanged = True
#
#         return sum(candies)


print(Solution.candy(0, [1,0,2]))