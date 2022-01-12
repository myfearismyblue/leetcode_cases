# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        answer = []
        letter_set = set()
        for idx in range(201):
            try:
                letter_set = set(strs[0][idx])
            except IndexError:
                return ''.join(answer)

            for word in strs:
                assert word.islower()
                letter_set.add(word[idx])
            if len(letter_set) == 1:
                answer.append(word[idx])
            elif len(letter_set) > 1:
                return ''.join(answer)
            else:
                assert True, "Impossible: if the letter set is empty, exception should be caught"


        return ''.join(answer)

strs = ["flower", "flow", "flight"]
# strs = ['car', 'cir']
my_sol = Solution()
print(my_sol.longestCommonPrefix(strs))
