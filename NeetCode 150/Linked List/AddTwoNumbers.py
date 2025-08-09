# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res = ListNode()
        current = res
        sum = 0
        carry = 0

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sum = num1 + num2 + carry

            carry = sum // 10
            num = sum % 10

            current.next = ListNode(num)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return res.next
