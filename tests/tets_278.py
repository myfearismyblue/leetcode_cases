# Example 1:
#
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:
#
# Input: n = 1, bad = 1
# Output: 1

# Constraints:
#
# 1 <= bad <= n <= 231 - 1

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

from _278_First_Bad_Version import Solution, isBadVersion_wrapper
import pytest

my_sol = Solution()


@pytest.mark.parametrize("n, expected", [(50, 35),
                                         # (1, 1),
                                         ])
def test_firstBadVersion(n, expected):
    assert my_sol.firstBadVersion(n) == expected
