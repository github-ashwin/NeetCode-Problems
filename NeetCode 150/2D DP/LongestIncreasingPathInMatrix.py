from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        DFS through the matrix
        Find the longest path at each position and store it in the hashmap
        """
        rows,cols = len(matrix),len(matrix[0])

        hm={}

        def dfs(r,c,prev):
            if(r<0 or r==rows or c<0 or c==cols or matrix[r][c]<=prev):
                return 0
            if(r,c) in hm:
                return hm[(r,c)]

            result = 1
            result = max(result, 1 + dfs(r+1, c, matrix[r][c]))
            result = max(result, 1 + dfs(r-1, c, matrix[r][c]))
            result = max(result, 1 + dfs(r, c+1, matrix[r][c]))
            result = max(result, 1 + dfs(r, c-1, matrix[r][c]))
            hm[(r,c)] = result
            return result

        for row in range(rows):
            for col in range(cols):
                dfs(row,col,-1)

        return max(hm.values())

        