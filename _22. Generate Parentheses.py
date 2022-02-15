# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

class Solution:
    def generateParenthesis(self, n: int):
        class ParenthesisStringStack:
            def __init__(self, string):
                self.string = string
                self.stack_level, _ = self._get_stack_level()
                self.valid = self.is_valid()

            def _get_stack_level(self):
                """Changes stack_level while iterating string. Returns level and if stack_level was ever lower zero"""
                stack_level = 0
                always_been_valid = True
                for item in self.string:
                    assert item in ['(', ')']
                    stack_level = stack_level + 1 if item == '(' else stack_level - 1
                    always_been_valid = always_been_valid and (stack_level >= 0)
                return stack_level, always_been_valid

            def is_valid(self):
                """Returns if the current state is valid like '()()(())' """
                level, always_been_valid = self._get_stack_level()
                if not level and always_been_valid:
                    return True
                return False

            def join_left_parth(self):
                """Creates a new object ParenthesisStringStack with '(' joined at the end"""
                new_string = ParenthesisStringStack(self.string)
                new_string.string = ''.join([new_string.string, '('])
                new_string.stack_level, _ = new_string._get_stack_level()
                new_string.valid = new_string.is_valid()
                return new_string

            def join_right_parth(self):
                """Creates a new object ParenthesisStringStack with ')' joined at the end"""
                new_string = ParenthesisStringStack(self.string)
                new_string.string = ''.join([new_string.string, ')'])
                new_string.stack_level, _ = new_string._get_stack_level()
                new_string.valid = new_string.is_valid()
                return new_string

        def create_parenthesis_pool(depth):
            return ['('] * depth, [')'] * depth

        left_parth, right_parth = create_parenthesis_pool(n)

        def generate_substrings(previous_substring, left_parth, right_parth):
            """Generates valid string recurrently"""
            assert previous_substring.stack_level >= 0
            if not left_parth and not right_parth and previous_substring.valid:
                nonlocal answer
                return answer.append(previous_substring.string)

            if not previous_substring.stack_level and left_parth:
                assert right_parth
                new_substring = previous_substring.join_left_parth()
                generate_substrings(new_substring, left_parth[:-1], right_parth)
            elif previous_substring.stack_level:
                if left_parth:
                    new_substring = previous_substring.join_left_parth()
                    generate_substrings(new_substring, left_parth[:-1], right_parth)
                if right_parth:
                    new_substring = previous_substring.join_right_parth()
                    generate_substrings(new_substring, left_parth, right_parth[:-1])

        answer = []

        generate_substrings(ParenthesisStringStack(''), left_parth, right_parth)

        return answer


my_sol = Solution()
n = 4
print(my_sol.generateParenthesis(n))
