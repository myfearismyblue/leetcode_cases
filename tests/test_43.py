# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Constraints:
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
import pytest
from _43_Multiply_Strings import Solution

my_sol = Solution()


@pytest.mark.parametrize("num1, num2, expected", [('0', '1', '0'),
                                                  ('111', '111', '12321'),
                                                  ('10', '0', '0'),
                                                  ])
def test_multiply(num1, num2, expected):
    assert my_sol.multiply(num1, num2) == expected


@pytest.mark.parametrize("num1, num2, expected_exception", [('01', '1', AssertionError),
                                                            ('1', '01', AssertionError),
                                                            ('ac', '1', AssertionError),
                                                            ('-1', '1', AssertionError),
                                                            ('0', '01', AssertionError),
                                                            ('0', 'a', AssertionError),
                                                            ('', '', AssertionError),
                                                            ('1' * 201, '1', AssertionError),
                                                            ])
def test_multiply_exceptions(num1, num2, expected_exception):
    with pytest.raises(expected_exception):
        my_sol.multiply(num1, num2)


@pytest.mark.parametrize("num, expected", [(str(num), [num]) for num in range(9)] +         # ('0', [0]), ('1', [1]), ..
                         [('1234567890', list(map(int, '1234567890'))),
                          ])
def test_string_to_digit_list(num, expected):
    assert my_sol.string_to_digit_list(num) == expected


@pytest.mark.parametrize("num_list, expected", [([1, 2, 3], 123),
                                                ([1], 1),
                                                ])
def test_number_list_to_int(num_list, expected):
    assert my_sol.number_list_to_int(num_list) == expected


@pytest.mark.parametrize("num, expected", [(1230, '1230'),
                                           (0, '0'),
                                           (1, '1'),
                                           ])
def test_int_to_string(num, expected):
    assert my_sol.int_to_string(num) == expected
