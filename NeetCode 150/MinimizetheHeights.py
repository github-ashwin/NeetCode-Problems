class Solution:
    def getMinDiff(self, arr, k):
        # code goes here
        # sort the array
        arr.sort()
        n = len(arr)
        
        current_hdiff = arr[-1] - arr[0]
        small = arr[0] + k
        large = arr[-1] - k
        
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            
            current_min = min(small, arr[i] - k)
            current_max = max(large, arr[i - 1] + k)
            
            current_hdiff = min(current_hdiff, current_max - current_min)
        
        return current_hdiff
