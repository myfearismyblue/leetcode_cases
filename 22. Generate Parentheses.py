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
                level, always_been_valid = self._get_stack_level()
                if not level and always_been_valid:
                    return True
                return False

            def append_left(self):
                self.string = ''.join([self.string, '('])
                self.stack_level, _ = self._get_stack_level()
                self.valid = self.is_valid()

            def append_right(self):
                self.string = ''.join([self.string, ')'])
                self.stack_level, _ = self._get_stack_level()
                self.valid = self.is_valid()

        def create_parenthesis_pool(depth):
            left_pars = ['(' for i in range(depth)]
            right_pars = [')' for i in range(depth)]
            return left_pars, right_pars

        left_pars, right_pars = create_parenthesis_pool(n)



        my_string = ValidString('(()')
        print(my_string.append_right())

        answer = []

        return answer


my_sol = Solution()
n = 3
my_sol.generateParenthesis(n)
print()
