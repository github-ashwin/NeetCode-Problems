#User function Template for python3

class Solution:
    def toyCount(self, N, K, arr):
        # code here
        
        arr.sort()
        
        count = 0
        total = 0
        
        for price in arr:
            if total+price <= K:
                count+=1
                K-=price
            else:
                break
        
        return count
