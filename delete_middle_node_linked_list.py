"""
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""
from __future__ import annotations
from typing import Optional


class ListNode:
    val: int
    next: Optional[ListNode] = None
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = head
        fast = slow.next.next if slow.next else None
        
        while fast and fast.next:
            slow = slow.next if slow else None
            fast = fast.next.next
        
        if not slow:
            raise ValueError('')
        
        slow.next = slow.next.next if slow.next else None

        return head