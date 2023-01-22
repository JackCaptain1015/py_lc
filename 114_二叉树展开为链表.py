# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    直接先求前序遍历，最后节点依次往后处理
    '''
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def back(node):
            if not node:
                return ;
            ansArr.append(node);
            back(node.left);
            back(node.right);
        if not root:
            return None;
        ansArr = [];
        back(root);
        for i in range(len(ansArr)):
            if i == len(ansArr)-1:
                ansArr[i].left = None;
                ansArr[i].right = None;
                continue;
            ansArr[i].left = None;
            ansArr[i].right = ansArr[i+1];


