# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        
        l2r = {}
        r2l = {}
        
        total = 0
        
        for i in range(len(arr)):
            total+=arr[i]
            l2r[i]=total
        
        total = 0
        
        for i in range(len(arr)-1,-1,-1):
            total+=arr[i]
            r2l[i]=total
        
        for i in range(len(arr)):
            if l2r[i] == r2l[i]:
                return i
        return -1

