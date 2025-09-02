from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        result = []
        n = len(arr)
        # for i in range(n-k+1):
        #     result.append(max(arr[i:i+k]))
        
        # return result
        
        dq = deque()
        
        for i in range(n):
            
            if dq and dq[0]<=i-k:
                dq.popleft()
            
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
                
            dq.append(i)
            
            if i >= k-1:
                result.append(arr[dq[0]])
            
        return result
