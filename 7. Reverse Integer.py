# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        reverse = sign * int(str(x)[::-1])
        return reverse if -2 ** 31 <= reverse <= 2 ** 31 - 1 else 0


x = 123
my_sol = Solution()
print(my_sol.reverse(x))
