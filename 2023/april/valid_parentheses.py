"""
We know a parentheses is valid if the number of open parentheses matches the number of close parentheses.

So, you want to iterate through the string to ensure there is a complete match.

The easiest way to do this is using a stack data structure.
- Create a stack
- Iterate through the string
- If left parentheses, push to stack
- If right parentheses:
    - If stack is empty, return false (there HAS to be a left parentheses before a right parentheses)
    - If stack is not empty,
        - If the parentheses at the top of the stack matches the right parentheses, pop the stack
        - Otherwise, return false (parentheses MUST match)

- Once you've finished iterating through the string, if there are still parentheses in the stack, return False
- Otherwise, return true


"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        right_to_left_parens = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for c in s:
            if c in right_to_left_parens:
                if len(stack) > 0 and stack[-1] == right_to_left_parens[c]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(c)

        return True if len(stack) == 0 else False
