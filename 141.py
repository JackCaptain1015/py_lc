# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head;
        while node and node.next and node.next.next:
            node = node.next.next;
            head = head.next;
            if node == head :
                return True;
        return False;
