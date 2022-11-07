# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseSon(self, head: ListNode, tail: ListNode):
        pre = tail.next;
        cur = head;
        # 这里不能是cur != tail，因为pre在cur上一位，如果是cur的话，最终执行会少执行一次
        while pre != tail:
            next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;
        return tail, head;

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        headPre = ListNode(0)
        # headPre.next指向了head，随着head的变化,head依旧是头部
        headPre.next = head
        # pre表示前一个子链的尾部节点
        pre = headPre
        while head:
            # sonTail必须从pre开始，如果从head开始的话，经过k次，那么会发现多走了一步
            sonTail = pre
            # 翻转子链
            for i in range(k):
                sonTail = sonTail.next
                if not sonTail:
                    return headPre.next
            nex = sonTail.next
            # 翻转子链后，head为sonTail
            head, sonTail = self.reverse(head, sonTail)
            # 把子链与上个子链接上
            pre.next = head
            # 把子链与下个子链接上
            sonTail.next = nex
            # 重新赋值，开始下一轮
            pre = sonTail
            head = sonTail.next

        return headPre.next




##不实际交换node而是只改变值
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lNode,rNode = head,head;
        kList = [];
        count = 0;
        while rNode:
            kList.append(rNode.val);
            count += 1;
            rNode = rNode.next;
            if count == k:
                for i in range(0,len(kList)):
                    lNode.val = kList.pop();
                    lNode = lNode.next;
                count = 0;
        return head;

