"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    '''
    思路，因为random可能指向前面的节点，所以要有个map，key是原来的节点，val是复制后的节点，这样
    复制节点都存在后，再遍历一次原链表设置next与random
    '''
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head;
        copyNodeMap = {}
        dummyNode = Node(0);
        preNode = head;
        while preNode:
            copyNodeMap[preNode] = Node(preNode.val);
            preNode = preNode.next;
        preNode = head;
        i = 0;
        while preNode:
            temp = copyNodeMap[preNode];
            if i == 0:
                dummyNode.next = temp;
            temp.next = copyNodeMap[preNode.next] if preNode.next and copyNodeMap.get(preNode.next) else None;
            temp.random = copyNodeMap[preNode.random] if preNode.random and copyNodeMap.get(preNode.random) else None;
            preNode = preNode.next;
            i += 1;
        return dummyNode.next;



