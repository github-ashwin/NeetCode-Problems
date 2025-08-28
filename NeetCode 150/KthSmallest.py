#User function Template for python3
import heapq

class Solution:

    def kthSmallest(self, arr,k):
        
        # Priority queue approach
        heapq.heapify(arr) # heapify
        """
        index = i
        leftchild = (2*i)+1
        rightchild = (2*i)+2
        parent = (i-1)/2
        """
        for i in range(k-1):
            heapq.heappop(arr)
        
        return heapq.heappop(arr)
