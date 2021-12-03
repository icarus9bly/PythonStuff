# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true
class Solution:
    def isValid(self, s: str) -> bool:
        """
        1: Pop the string stack
        2: If poped element in TBD

        """
        stack = []
        validation = True
        list_s = list(s)  # ['{', '[', ']', '}']
        open_brackets = ['{', '(', '[']
        closed_brackets = ['}', ')', ']']
        pair = {']': '[',
                ')': '(',
                '}': '{'
                }
        for char in list_s:
            # Add open bracket to the stack
            if char in open_brackets:
                stack.append(char)
            # If stack not empty and closed bracket is same as last elem in stack remove last open bracket from stack
            if char in closed_brackets:
                if stack and pair[char] == stack[-1]:
                    stack.pop()
                else:
                    validation = False
        if stack:
            validation = False
        return validation
