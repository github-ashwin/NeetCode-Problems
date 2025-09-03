'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    def removeLoop(self, head):
        # code here
        
        # Floyd's cycle detection method
        # Find if there's a loop
        
        if not head and head.next:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
            
        else:
            return False
        
        # Find the loop start
        slow = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
            
        # Change the loop
        
        temp = slow
        while temp.next!=slow: # Not pointing back to the original node (i.e. loop)
            temp = temp.next
        
        temp.next = None
        
        return True
        
