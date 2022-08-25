def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    # 如果左树不存在公共祖先，就返回右树
    if not left:
        return right
    if not right:
        return left
    #都不存在就返回root（因为前提是必然存在）
    return root


----------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getSon(self, root: 'TreeNode',p: 'TreeNode', q: 'TreeNode'):
        res = [];
        leftRes = [];
        rightRes = [];
        if root.left:
            leftRes,ans = self.getSon(root.left,p,q);
            if ans:
                return leftRes,ans;
            if p.val in leftRes and q.val in leftRes:
                return leftRes,root.left;
        if root.right:
            rightRes,ans = self.getSon(root.right,p,q);
            if ans:
                return rightRes,ans;
            if p.val in rightRes and q.val in rightRes:
                return rightRes,root.right;
        res.append(root.val);
        res = res + leftRes;
        res = res + rightRes;
        if p.val in res and q.val in res:
            return res,root;
        return res,None;
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res,ans = self.getSon(root,p,q);
        return ans;
