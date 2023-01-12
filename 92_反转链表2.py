# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head;
        dummyHead = ListNode();
        dummyHead.next = head;
        tempNode = dummyHead;
        #因为tempNode是从dummyHead开始的，所以要走range(left-1)，
        # 如果是从head开始，那走range(left-2)才会到反转链表的上一个节点
        for i in range(left-1):
            tempNode = tempNode.next;

        curNode = tempNode.next;

        #比如1->2->3->4->5中需要反转2、3、4，那么先处理2的next，再处理3的next，
        # 最后处理1的next，注意，这里tempNode是不移动的（因为最后1要指向4），
        # 而curNode是对应的node也是不变的，只是位置不断改变
        #准确的说这不是节点间的交换，而是后面的节点不断往前面插入
        for i in range(right-left):
            nextNode = curNode.next;
            curNode.next = nextNode.next;
            nextNode.next = tempNode.next;
            tempNode.next = nextNode;
        return dummyHead.next;


