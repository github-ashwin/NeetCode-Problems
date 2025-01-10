from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #using hashmap {key:column number,value:set of values}

        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row]) or (board[row][col] in columns[col]) or (board[row][col] in squares[(row//3,col//3)]):
                    return False
                    
                columns[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row//3,col//3)].add(board[row][col])
        return True


        