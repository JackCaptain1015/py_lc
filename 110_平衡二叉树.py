# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    自底向上递归，一开始先递归到叶子节点，然后按max(leftDeep,rightDeep)+1开始
    逐步网上计算深度，这样一开始leftDeep与rightDeep相差超过1就能立马看出来。
    最后只要返回的结果不是-1就是平衡二叉树（空树也算平衡二叉树）
    '''
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def back(node):
            if not node:
                return 0;
            leftDeep = back(node.left);
            rightDeep = back(node.right);
            if leftDeep == -1 or rightDeep == -1 or abs(leftDeep-rightDeep) > 1:
                return -1;
            return max(leftDeep,rightDeep)+1;

        return back(root)>=0;