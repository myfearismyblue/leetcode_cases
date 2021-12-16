# You are given a string s. You can convert s to a palindrome by adding characters in front of it.
#
# Return the shortest palindrome you can find by performing this transformation.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # The common formula of such palindrome: BxOyA, where xOyA == s, and x - is the left root,
        # y == left_root[::-1] -
        # mirrored part of the root (right), O - is a sliding middle pointer iterating through
        # [s[0], '', s[1], ''....],
        # A - is a remaining suffix of the string
        # B == remaining_suffix[::-1],
        answer = s[::-1] + s                                    # at least
        if not s:
            return answer
        for idx in range(0, len(s) // 2 + 1):
            # idx is the sliding pointer of middle

            # The first case: middle_pointer points to an char
            middle_pointer = s[idx]
            left_root = s[:idx]
            y1 = s[idx+1:idx+1+len(left_root)]
            if left_root == y1[::-1]:
                right_root = y1
                remaining_suffix = s[idx + 1 + len(left_root):]
                answer = remaining_suffix[::-1] + left_root + middle_pointer + right_root + remaining_suffix \
                    if len(remaining_suffix[::-1] + left_root + middle_pointer +
                           right_root + remaining_suffix) < len(answer) else answer

            # The second case: middle_pointer points to '' between chars
            middle_pointer = ''
            left_root = s[:idx+1]
            y2 = s[idx + 1:idx + 1 + len(left_root)]
            if left_root == y2[::-1]:
                right_root = y2
                remaining_suffix = s[idx + 1 + len(left_root):]
                answer = remaining_suffix[::-1] + left_root + middle_pointer + right_root + remaining_suffix \
                    if len(remaining_suffix[::-1] + left_root + middle_pointer +
                           right_root + remaining_suffix) < len(answer) else answer

        return answer


my_sol = Solution()

s = 'aaccf'
print(my_sol.shortestPalindrome(s))
