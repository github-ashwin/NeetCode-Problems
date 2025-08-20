from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left, right = 0, n*m - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, m)
            mid_val = matrix[row][col]

            if mid_val == target:
                return True

            # Values at search boundaries
            left_val = matrix[left // m][left % m]
            right_val = matrix[right // m][right % m]

            # Left half is sorted
            if left_val <= mid_val:
                if left_val <= target < mid_val:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if mid_val < target <= right_val:
                    left = mid + 1
                else:
                    right = mid - 1

        return False