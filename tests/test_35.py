import pytest
from _35_Search_Insert_Position import Solution

my_solution = Solution()

@pytest.mark.parametrize("nums, target, expected", [([1, 3, 5, 6], 5, 2),
                                                    ([1, 3, 5, 6], 2, 1),
                                                    ([1, 3, 5, 6], 7, 4),
                                                    ([1], -1, 0),
                                                    ([5], 7, 1),
                                                    ])
def test_searchInsert(nums, target, expected):
    assert my_solution.searchInsert(nums, target) == expected
