# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
# Example 1:
#
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
from typing import List


class Solution:
    def string_to_digit_list(self, num: str) -> List[int]:
        assert num.isnumeric() and 1 <= len(num) <= 200
        assert num[0] != '0' if len(num) > 1 else True                     # no leading zero
        result = []
        [result.append(ord(char) - 48) for char in num]                    # ord('0') == 48
        return result

    def number_list_to_int(self, number_list: List[int]) -> int:
        number = 0
        for position in range(len(number_list) - 1, -1, -1):
            number += number_list[position] * 10 ** (len(number_list) - 1 - position)
        return number

    def int_to_string(self, num: int) -> str:
        if not num:
            return '0'
        result = ''
        temp_num = num
        while temp_num:
            current_digit = temp_num % 10
            temp_num = temp_num // 10
            result = ''.join(chr(current_digit + 48) + result)
        return result

    def multiply(self, num1: str, num2: str) -> str:
        return self.int_to_string((self.number_list_to_int(self.string_to_digit_list(num1)) *
                                   self.number_list_to_int(self.string_to_digit_list(num2))))
