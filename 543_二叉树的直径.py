# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    '''
    深度遍历，思路是经过的节点数-1即为最大路径，ans即为节点数，所以
    leftAns+rightAns+1即左子树节点+右子树节点+当前子树根节点，
    而back()返回的是子树下路径最长的节点数+子树根节点。
    易错点要注意，基本类型在函数外部的定义，要用self引用
    '''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def back(root):
            if not root:
                return 0;
            leftAns = back(root.left);
            rightAns = back(root.right);
            self.ans = max(self.ans,leftAns+rightAns+1);
            return max(leftAns,rightAns)+1;
        self.ans = 1;
        back(root)
        return self.ans-1;