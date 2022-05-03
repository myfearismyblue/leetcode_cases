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

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        assert 1 <= len(nums) <= 1000
        ret = [nums[0]]
        for num in nums[1:]:
            assert -10 ** 6 <= num <= 10 ** 6
            ret.append(ret[-1] + num)
        return ret

my_sol = Solution()
print(my_sol.runningSum(
    [34, -13, 12, -59, 27, -63, 1, 94, 84, 54, 9, 57, 53, 11, 85, -17, -78, -85, -84, 5, 43, -44, -48, -38]))