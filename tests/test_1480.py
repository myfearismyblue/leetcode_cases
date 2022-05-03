# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:
#
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:
#
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
# Constraints:
#
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6

import pytest
from typing import List

from _1480_Running_Sum_of_1d_Array import Solution

my_sol = Solution()


@pytest.mark.parametrize('nums, expection',
                         [([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
                          ([3,1,2,10,1], [3,4,6,16,17]),
                          ([1,2,3,4], [1, 3, 6, 10]),
                          ([[34,-13,12,-59,27,-63,1,94,84,54,9,57,53,11,85,-17,-78,-85,-84,5,43,-44,-48,-38]], [-7])
                          ]
                         )
def test_runningSum(nums: List[int], expection):
    assert my_sol.runningSum(nums) == expection
