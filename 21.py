# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #preHead与prev用的是相同的引用，也就是说prev指向下一个时preHead也指向了下一个
        #直到prev = prev.next后，两者才分开
        preHead = ListNode(-1);
        prev = preHead;

        while list1 and list2:
            if list1.val > list2.val:
                prev.next = list2;
                list2 = list2.next;
            else:
                prev.next = list1;
                list1 = list1.next;
            prev = prev.next;
        prev.next = list1 if list1 is not None else list2;
        return preHead.next;
