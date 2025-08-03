class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {'(': ')', '[': ']', '{': '}'} # Valid Parenthesis pairs
        for c in s:
            if c in chars: # Checks if thr character is valid, then adds
                stack.append(c)
            else:
                if not stack or chars[stack.pop()]!=c: # If not valid or not the right sequence, return False
                    return False
        return not stack
