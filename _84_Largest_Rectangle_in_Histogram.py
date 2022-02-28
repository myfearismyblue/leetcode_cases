# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Input: heights = [2,4]
# Output: 4

# Constraints:
#
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        for idx, height in enumerate(heights):
            left_boundary = 0
            if idx:
                for jdx, left in zip(range(idx, 0, -1), heights[idx - 1::-1]): # search for left boundary
                    if left < height:
                        left_boundary = jdx
                        break
            right_boundary = len(heights) - 1
            for jdx, right in enumerate(heights[idx+1:], start=idx+1):             # search for right boundary
                if right < height:
                    right_boundary = jdx - 1
                    break
            current_area = (right_boundary - left_boundary + 1) * height
            largest = max(largest, current_area)
        return largest

my_sol = Solution()
print(my_sol.largestRectangleArea([2,1,5,6,2,3]))
