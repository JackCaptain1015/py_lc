# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    思路不复杂，主要是绕，关键点在于curNode.next and curNode.next.val == curNextVal
    '''
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None;
        dummyNode = ListNode(0,head);
        curNode = dummyNode;
        while curNode.next and curNode.next.next:
            if curNode.next.val == curNode.next.next.val:
                curNextVal = curNode.next.val;
                while curNode.next and curNode.next.val == curNextVal:
                    curNode.next = curNode.next.next;
            else:
                curNode = curNode.next;
        return dummyNode.next;




