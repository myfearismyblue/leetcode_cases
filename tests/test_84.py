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
import pytest
from typing import List
from _84_Largest_Rectangle_in_Histogram import Solution

my_sol = Solution()


@pytest.mark.parametrize("heights, expected", [([2, 1, 5, 6, 2, 3], 10),
                                               ([2, 4], 4),
                                               ([0], 0),
                                               ([2, 1, 2, 1, 2, 1], 6),
                                               ([1, 2, 3, 4, 5, 6, 7], 16),
                                               ([7, 6, 5, 4, 3, 2, 1], 16),
                                               ([7, 6, 5, 4, 5, 6, 7], 28)
                                               ])
def test_largestRectangleArea(heights: List[int], expected: int):
    assert my_sol.largestRectangleArea(heights) == expected
