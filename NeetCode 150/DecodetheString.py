class Solution:
    def decodedString(self, s):
        # code here
        
        stack = []
        
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substring = ""
                
                while stack and stack[-1] != '[':
                    substring=stack.pop() + substring
                stack.pop()
                
                numstr = ""
                
                while stack and stack[-1].isdigit():
                    numstr=stack.pop() + numstr
                num = int(numstr)
                
                stack.append(substring*num)
        
        return "".join(stack)
                
                
