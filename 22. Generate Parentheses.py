# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

class Solution:
    def generateParenthesis(self, n: int):
        class ValidString:

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

            def append_left(self):
                new_string = ValidString(self.string)
                new_string.string = ''.join([new_string.string, '('])
                new_string.stack_level, _ = new_string._get_stack_level()    # FIXME: to check if it's ok to increase
                new_string.valid = new_string.is_valid()                     # stack_level only w/o calculating
                return new_string

            def append_right(self):
                new_string = ValidString(self.string)
                new_string.string = ''.join([new_string.string, ')'])
                new_string.stack_level, _ = new_string._get_stack_level()   # FIXME: to check if it's ok to decrease
                new_string.valid = new_string.is_valid()                    # stack_level only w/o calculating
                return new_string

        def create_parenthesis_pool(depth):
            left_pars = ['(' for i in range(depth)]
            right_pars = [')' for i in range(depth)]
            return left_pars, right_pars

        left_pars, right_pars = create_parenthesis_pool(n)

        def generate_substrings(previous_substring, left_pars, right_pars):
            assert previous_substring.stack_level >= 0
            if not left_pars and not right_pars and previous_substring.valid:
                nonlocal answer
                return answer.append(previous_substring)

            if not previous_substring.stack_level and left_pars:
                assert right_pars
                new_substring = previous_substring.append_left()
                generate_substrings(new_substring, left_pars[:-1], right_pars)

            elif previous_substring.stack_level:
                if left_pars:
                    new_substring = previous_substring.append_left()
                    generate_substrings(new_substring, left_pars[:-1], right_pars)
                if right_pars:
                    new_substring = previous_substring.append_right()
                    generate_substrings(new_substring, left_pars, right_pars[:-1])

        answer = []

        generate_substrings(ValidString(''), left_pars, right_pars)

        return answer


my_sol = Solution()
n = 3

[print(item.string) for item in my_sol.generateParenthesis(n)]
