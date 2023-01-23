# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head and not head.next:
            return True;
        arr = [];
        preNode = head;
        while preNode:
            arr.append(preNode.val);
            preNode = preNode.next;
        size = len(arr);

        for i in range(size // 2):
            if arr[i] != arr[size-i-1]:
                return False;
        return True;