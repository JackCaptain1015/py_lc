# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        hasTen = False;
        dummyNode,temp = ListNode(0),ListNode(0);
        dummyNode.next = temp;
        while l1 and l2:
            val = l1.val + l2.val;
            if hasTen:
                val += 1;
                hasTen = False;
            if val > 9:
                hasTen = True;
                val -= 10;
            node = ListNode(val);
            temp.next = node;
            temp = temp.next;
            l1 = l1.next;
            l2 = l2.next;
        while l1:
            val = l1.val;
            if hasTen:
                val += 1;
                hasTen = False;
            if val > 9:
                hasTen = True;
                val -= 10;
            node = ListNode(val);
            temp.next = node;
            temp = temp.next;
            l1 = l1.next;
        while l2:
            val = l2.val;
            if hasTen:
                val += 1;
                hasTen = False;
            if val > 9:
                hasTen = True;
                val -= 10;
            node = ListNode(val);
            temp.next = node;
            temp = temp.next;
            l2 = l2.next;
        if hasTen:
            node = ListNode(1);
            temp.next = node;
        return dummyNode.next.next;

