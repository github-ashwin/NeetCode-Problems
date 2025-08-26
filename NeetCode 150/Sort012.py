class Solution:
    def sort012(self, arr):
        # code here
        # Dutch National Flag Algorithm
        
        low = 0
        mid = 0
        high = len(arr)-1
        
        while mid <= high:
            
            if arr[mid] == 0:
                arr[low],arr[mid] = arr[mid],arr[low]
                low+=1
                mid+=1
            elif arr[mid] == 1:
                mid+=1
            else:
                if mid != high:
                    arr[mid],arr[high] = arr[high],arr[mid]
                high-=1

