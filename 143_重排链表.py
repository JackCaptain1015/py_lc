# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
            整体思路就是先遍历链表将节点全部存到列表中，然后把尾部的节点拿来
            放到头部节点的后面（注意这时候是节点的next操作，而不是操作数组），
            最后判断i==j的的节点会变成尾节点，尾节点的next为None
        '''
        if not head:
            return;
        arr = list();
        node = head;
        while node:
            arr.append(node);
            node = node.next;
        i,j = 0,len(arr)-1;
        while i < j :
            arr[i].next = arr[j];
            arr[j].next = arr[i+1];
            i += 1;
            j -= 1;
        arr[i].next = None;




