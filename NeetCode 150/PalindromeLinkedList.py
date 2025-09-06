'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        # code here
        nums = []
        
        while not head:
            return -1
        
        temp = head
        
        while temp is not None:
            
            nums.append(temp.data)
            temp = temp.next
        
        if nums == nums[::-1]:
            return True
        else:
            return False
            
        
        
