
from typing import List


class Solution:
    def zigZag(self,arr : List[int]) -> None:
        # code here
        n = len(arr)
        
        if n <= 2:
            return True
         
        # rearragnge 
        for i in range(n - 1):
            if i % 2 == 0:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]

        #  validate zigzag
        for i in range(n - 1):
            if i % 2 == 0:
                if arr[i] >= arr[i+1]:
                    return False
            else:
                if arr[i] <= arr[i+1]:
                    return False

        return True
