# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        map = dict();
        nodeA,nodeB = headA,headB;
        ans = None;
        while nodeA:
            map[nodeA] = nodeA;
            nodeA = nodeA.next;
        while nodeB:
            '''注意，py3中dict的获取操作一定要用get,
            直接获取的话，如果key不存在会报错'''
            if map.get(nodeB):
                ans = map[nodeB];
                break;
            nodeB = nodeB.next;
        return ans;
