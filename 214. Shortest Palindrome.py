# You are given a string s. You can convert s to a palindrome by adding characters in front of it.
#
# Return the shortest palindrome you can find by performing this transformation.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # The common formula of such palindrome: BxOyA, where xOyA == s, and x - is the 'root' and always x[0] == s[0],
        # y == x[::-1] - mirrored part of the root of initial string, O - is any char including '', B == A[::-1],
        # A - is a remaining part
        # For any string s, A at least is A == s[1:]
        A = s[1:]
        O = ''

        for idx in range(1, len(s) // 2):
            # x[0] == s[0], x[-1] == s[idx], idx is the right bound of root x
            x = s[:idx]
            y1 = s[idx:idx+len(x)]                                  #FIXME: check ranges
            y2 = s[idx+1:idx+1+len(x)]                              #FIXME: check ranges
            if x == y1[::-1]:
                y = y1
                A = s[idx + len(x):]                                # O remain empty ''
            elif x == y2[::-1]:
                y = y2
                A = s[idx + 1 + len(x):]
                O = s[idx]

        return A[::-1] + x + O + y + A


my_sol = Solution()

s = 'aacd'
print(my_sol.shortestPalindrome(s))
