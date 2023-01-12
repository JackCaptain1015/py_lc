# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    自顶向下归并排序，整体思路就是递归拆分到最后，然后合并。主要是要注意细节，
    比如tail节点不处理，所以head.next == tail要跳出，因为拆分后tail不一定为None，
    所以不能是fast not None判断，而是fast != tail，最后merge中，要注意dummyNode
    与temp，dummyNode不走，主要是temp往下走
    '''
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.sortFun(head,None);
    def sortFun(self,head,tail):
        if not head:
            return head;
        #tail节点不处理，用于下面递归，所以两边都是用的mid，而不是mid与mid.next
        if head.next == tail:
            head.next = None;
            return head;
        slow,fast = head,head;
        while fast != tail:
            slow = slow.next;
            fast = fast.next;
            if fast != tail:
                fast = fast.next;
        mid = slow;
        return self.merge(self.sortFun(head,mid),self.sortFun(mid,tail));

    def merge(self,node1,node2):
        dummyNode = ListNode();
        temp,temp1,temp2 = dummyNode,node1,node2;
        while temp1 and temp2:
            if temp1.val > temp2.val:
                temp.next = temp2;
                temp2 = temp2.next;
            else:
                temp.next = temp1;
                temp1 = temp1.next;
            temp = temp.next;
        if temp1:
            temp.next = temp1;
        if temp2:
            temp.next = temp2;
        return dummyNode.next;

