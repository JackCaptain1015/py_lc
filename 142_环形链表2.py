# Definition for singly-linked list.
from typing import Optional
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    字典，快慢指针的方法太麻烦了，主要是公式的推导，字典反而好用
    '''
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        map = dict();
        while head:
            if not map.get(head):
                map[head] = 1;
            else:
                return head;
            head = head.next;
        return None;

