"""
So, the intuition behind this is similar to Valid Parentheses, except now you need to return a string with only valid parentheses

First, in order to do that, you need to know which parentheses make this string an invalid parentheses

Then, once you know where the 'bad parentheses' are, you need to make sure you don't include them into the string

Just popping from the string won't work, as that requires a lot of runtime

Instead, you'll need to construct a new string and skip the 'bad parentheses indeces'

Like our previous problem, we will make a stack
But this time, we'll push the indeces to the stack (since there is only one type of parentheses)

Then we iterate over the string again, and skip the indeces that have been identified as 'bad parentheses'


"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        bad_parens_indeces = set()
        stack = []
        output_chars = []

        for index in range(len(s)):
            if s[index] == ')':
            
                if stack:
                    stack.pop()

                else:
                    bad_parens_indeces.add(index)

            elif s[index] == '(':
                stack.append(index)

        if stack:
            for index in stack:
                bad_parens_indeces.add(index)

        for index in range(len(s)):
            if index not in bad_parens_indeces:
                output_chars.append(s[index])

        return ''.join(output_chars)
