# Example 1:
#
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.
# Example 2:
#
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

# Constraints:
#
# 1 <= n <= 30

import pytest
from _38_Count_and_Say import Solution

my_sol = Solution()


@pytest.mark.parametrize('array, expected', [('111', '31'),
                                             ('1', '11'),
                                             ('112233', '212223'),
                                             ('3322251', '23321511'),
                                             ])
def test_sequence_conversion(array: str, expected: str):
    assert my_sol.sequence_conversion(array) == expected


@pytest.mark.parametrize('array, expected_exception', [('', AssertionError),
                                                       ('1a', AssertionError),
                                                       ])
def test_sequence_conversion_exceptions(array: str, expected_exception):
    with pytest.raises(expected_exception):
        my_sol.sequence_conversion(array)


@pytest.mark.parametrize('n, expected', [(1, '1'),
                                         (2, '11'),
                                         (3, '21'),
                                         (4, '1211')])
def test_countAndSay(n: int, expected: str):
    assert my_sol.countAndSay(n) == expected
