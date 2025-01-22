from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(OPEN, CLOSED):
            if OPEN == CLOSED == n:
                res.append("".join(stack))
                return

            if OPEN < n:
                stack.append("(")
                backtrack(OPEN + 1, CLOSED)
                stack.pop()
            if CLOSED < OPEN:
                stack.append(")")
                backtrack(OPEN, CLOSED + 1)
                stack.pop()

        backtrack(0, 0)
        return res