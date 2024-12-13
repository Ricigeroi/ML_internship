class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for char in s:
            if char in dict:
                stack.append(dict[char])
            elif not stack or (stack and stack.pop() != char):
                return False
        return True if not stack else False