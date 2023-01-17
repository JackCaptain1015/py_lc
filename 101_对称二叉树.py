# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    递归，主要是要想清楚递归的条件
    '''
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(leftNode,rightNode):
            if not leftNode and not rightNode:
                return True;
            if not leftNode or not rightNode:
                return False;
            return (leftNode.val == rightNode.val
            and check(leftNode.left,rightNode.right)
            and check(leftNode.right,rightNode.left));
        return check(root,root);