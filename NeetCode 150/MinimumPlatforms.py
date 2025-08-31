class Solution:    
    def findPlatform(self,arr,dep):
        # code here
        
        arr.sort()
        dep.sort()
        
        i = j = 0
        n = len(arr)
        
        min_platforms = 0
        current_platforms = 0
        
        while i<n and j<n:
            # checking for overlapping condition
            if arr[i] <= dep[j]:
                current_platforms+=1
                min_platforms = max(min_platforms,current_platforms)
                i+=1
            else:
                current_platforms-=1
                j+=1
        
        return min_platforms
                
