# You are given a string s. You can convert s to a palindrome by adding characters in front of it.
#
# Return the shortest palindrome you can find by performing this transformation.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # The common formula of such palindrome: BxOyA, where xOyA == s, and x - is the 'root',
        # y == x[::-1] - mirrored part of the root of initial string, O - is a sliding pointer iterating through
        # [s[0], '', s[1], ''....], B == A[::-1],
        # A - is a remaining part
        # For any string s, at least x == '', O == s[0], y == '', A == s[1:]
        answer = s[::-1] + s
        for idx in range(0, len(s) // 2 + 1):                           # FIXME: check ranges
            # idx is the sliding pointer of O

            # The first case: O points to an char
            O = s[idx]
            x = s[:idx]
            y1 = s[idx+1:idx+1+len(x)]
            if x == y1[::-1]:
                y = y1
                A = s[idx + 1 + len(x):]
                answer = A[::-1] + x + O + y + A if len(A[::-1] + x + O + y + A) < len(answer) else answer

            # The second case: O points to '' between chars
            O = ''
            x = s[:idx+1]
            y2 = s[idx + 1:idx + 1 + len(x)]
            if x == y2[::-1]:
                y = y2
                A = s[idx + 1 + len(x):]
                answer = A[::-1] + x + O + y + A if len(A[::-1] + x + O + y + A) < len(answer) else answer

        return answer


my_sol = Solution()

s = 'a'
print(my_sol.shortestPalindrome(s))
