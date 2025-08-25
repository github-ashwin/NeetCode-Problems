#User function Template for python3

class Solution:
    def minValue(self, arr1, arr2):
        #code here
        arr1.sort()
        arr2.sort(reverse=True)
        
        result = 0
        
        for i in range(len(arr1)):
            result+=arr1[i]*arr2[i]
        
        return result
        
