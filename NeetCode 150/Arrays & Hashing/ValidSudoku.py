from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Hashset for each row to check for duplicates
        # Hashset for each columns to check for duplicates
        # Hashset for checking each 3x3 grids
        
        columns = defaultdict(set) # Key = Col. no., Value = set
        rows = defaultdict(set) # Key = Row. no., Value = set
        grids = defaultdict(set) # Key = Grid. no., Value = set

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    if (board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in grids[(i//3,j//3)]):
                        return False
                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
                    grids[(i//3,j//3)].add(board[i][j])
        return True