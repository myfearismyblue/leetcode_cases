# Example 1:
#
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# Example 2:
#
# Input: intervals = [[1,4],[2,3]]
# Output: 1

# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# 0 <= li <= ri <= 10^5
# All the given intervals are unique.

from _1288_Remove_Covered_Intervals import Solution
import pytest

my_sol = Solution()


@pytest.mark.parametrize("intervals, expected", [([[1, 4], [3, 6], [2, 8]], 2),
                                                 ([[1, 4], [2, 3]], 1),
                                                 ([[0, 0]], 1),
                                                 ([[100, 101], [99, 102], [98, 102], [98, 103]], 1),
                                                 ])
def test_removeCoveredIntervals(intervals, expected):
    assert my_sol.removeCoveredIntervals(intervals) == expected


@pytest.mark.parametrize("intervals, expected_exception", [([], my_sol.ConstrainViolation),
                                                           ([[-1, 0]], my_sol.ConstrainViolation),
                                                           ([[0, 10**5 + 1]], my_sol.ConstrainViolation),
                                                           ([[0, 1, 2]], my_sol.ConstrainViolation),
                                                           ([[i, i+1] for i in range(1002)], my_sol.ConstrainViolation),
                                                           ([[1, 2], [1, 2]], my_sol.ConstrainViolation),
                                                           ])
def test_removeCoveredIntervals_exceptions(intervals, expected_exception):
    with pytest.raises(expected_exception):
        my_sol.removeCoveredIntervals(intervals)
