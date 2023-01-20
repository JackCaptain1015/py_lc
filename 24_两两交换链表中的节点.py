# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    '''
    思路，只要是链表节点交换，就一定又dummyNode跟preNode，然后一个节点
    一个节点指针依次处理，最后再处理preNode的next指针。
    '''
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head;
        dummyNode = ListNode(0,head);
        preNode = dummyNode;
        while preNode.next and preNode.next.next:
            temp = preNode.next.next;
            preNode.next.next = preNode.next.next.next;
            temp.next = preNode.next;
            preNode.next = temp;
            preNode = preNode.next.next;
        return dummyNode.next;

s = Solution()
node4=ListNode(4);
node3=ListNode(3,node4);
node2=ListNode(2,node3);
node1=ListNode(1,node2);
print(s.swapPairs(node1).val)