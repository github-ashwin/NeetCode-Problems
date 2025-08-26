class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        jumps = 1                # At least one jump is needed
        current_pos = arr[0]     # Current range you can reach with the current jump
        max_pos = arr[0]         # Farthest position you can reach at this point
        
        if arr[0] == 0:          # If you can't move anywhere from index 0
            return -1
        
        for i in range(1, n):
            
            if i == n - 1:       # If we've reached the last index
                return jumps
            
            max_pos = max(max_pos, i + arr[i])  # Update the farthest reachable position
            
            if i == current_pos: # If we have reached the end of the current jump range
                current_pos = max_pos  # Update current position to farthest we can go
                jumps += 1             # Increment jump count
                
            if current_pos <= i:       # If we can't progress further
                return -1
