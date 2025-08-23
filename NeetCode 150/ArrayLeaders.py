class Solution:
    def leaders(self, arr):
        # code here
        leader = []
        current_max = float('-inf')
        # start,end = 0,len(arr)+1
        # while arr[start:end]:
        #     current_max = max(arr[start:end])
        #     leader.append(current_max)
        #     start = arr[start:end].index(current_max) + 1
        # return leader
        
        for num in reversed(arr):
            if num >= current_max:
                current_max = num
                leader.append(current_max)
        
        return reversed(leader)
            
            
