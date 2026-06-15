"""
https://leetcode.com/problems/add-two-numbers/description/
"""


from typing import Optional
from math import floor

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0

        dummy = ListNode()
        cur = dummy
        
        l1_next = l1
        l2_next = l2
        
        while l1_next or l2_next or carry != 0:
            digit_l1 = l1_next.val if l1_next else 0
            digit_l2 = l2_next.val if l2_next else 0
            
            total = digit_l1 + digit_l2 + carry
            digit_result = total % 10
            carry = floor(total / 10)
            
            new_node = ListNode(digit_result)
            cur.next = new_node
            cur = new_node
            
            l1_next = l1_next.next if l1_next else None
            l2_next = l2_next.next if l2_next else None
        
        return dummy.next
