# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        preNode = None;
        # head最终赋值为nextNodeNone，所以返回为preNode
        while head is not None:
            # 首先要获取next节点，获取到以后当前节点就可以指向pre了
            # 指向后，当前节点就变成了pre，然后把head往next上移动
            nextNode = head.next;
            head.next = preNode;
            preNode = head;
            head = nextNode;
        return preNode;

