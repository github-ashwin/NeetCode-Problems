'''
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        if k>length:
            return -1
            
        temp = head
            
        for _ in range(length-k):
            temp=temp.next
        
        return temp.data
        
