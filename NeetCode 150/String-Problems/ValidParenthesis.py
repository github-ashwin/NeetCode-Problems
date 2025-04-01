class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_pairs = {')': '(', ']': '[', '}': '{'}  
        stack = []

        for char in s:
            if char in bracket_pairs.values():  
                stack.append(char)
            elif char in bracket_pairs:  
                if not stack or stack.pop() != bracket_pairs[char]:  
                    return False  

        return not stack  
