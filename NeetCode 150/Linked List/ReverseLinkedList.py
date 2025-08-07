# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # If LL is not empty
        if not head:
            return None

        # Two pointer approach
        prev = None
        current = head

        # If node is present
        while current:
            temp = current.next # Takes next value
            current.next = prev # Reversing the next of current pointer to previous
            prev = current # Changing the previous of next loop
            current = temp # Changing the current for next loop
        
        return prev