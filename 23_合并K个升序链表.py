# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''分治法，两两合并，注意lists里的为节点，而不是数组'''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.merge(lists,0,len(lists)-1)

    def merge(self, lists: List[Optional[ListNode]], l: int, r: int):
        if l == r:
            return lists[l];
        if l > r:
            return None;
        mid = (l+r) >> 1;
        return self.merge2Lists(self.merge(lists,l,mid),self.merge(lists,mid+1,r));

    def merge2Lists(self,lList:ListNode,rList:ListNode):
        lIndex,rIndex = 0,0;
        head = ListNode(0);
        tail = head;
        while lList and rList:
            if lList.val < rList.val:
                tail.next = lList;
                lList = lList.next;
            else:
                tail.next = rList;
                rList = rList.next;
            tail = tail.next;
        tail.next = lList if lList else rList;
        # while rList:
        #     tail.next = rList;
        #     rList = rList.next;
        #     tail = tail.next;
        # while lList:
        #     tail.next = lList;
        #     lList = lList.next
        #     tail = tail.next;
        return head.next;



