from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            # checks whether the character is operator or operand
            if ch not in {"+", "-", "*", "/"}:
                stack.append(int(ch))
            else:
                num2 = stack.pop() # num2 comes first
                num1 = stack.pop() # then num1

                if ch == '+':
                    stack.append(num1 + num2)
                elif ch == '-':
                    stack.append(num1 - num2)
                elif ch == '*':
                    stack.append(num1 * num2)
                elif ch == '/':
                    stack.append(int(num1 / num2))
        
        return stack[0]
