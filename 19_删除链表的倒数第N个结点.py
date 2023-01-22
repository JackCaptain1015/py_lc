# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    要知道删除节点，那就要知道删除节点的前一个，所以要给节点算下标，最后考虑
    边界的情况，如果是删除的倒数第一个节点，即头节点，那size肯定还大于1，所以
    head往后走一位，如果size == 1，说明整个链表都删了，返回None
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeMap = {};
        preNode = head;
        i = 1;
        while preNode:
            nodeMap[i] = preNode;
            preNode = preNode.next;
            i += 1;
        size = len(nodeMap);
        preNode = nodeMap.get(size-n);
        if preNode:
            preNode.next = preNode.next.next;
            return head;
        else:
            if size > 1:
                head = head.next;
                return head;
            else:
                return None;