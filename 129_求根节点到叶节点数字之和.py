# Definition for a binary tree node.
from typing import Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    递归，主要就是要清楚在结果加入之前进行拼接
    '''
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sum(root,s):
            if not root:
                return;
            s = s+str(root.val);
            if root and not root.left and not root.right:
                ansArr.append(s);
                return;
            sum(root.left,s);
            sum(root.right,s);
        ansArr = [];
        sum(root,"");
        ans = 0;
        for temp in ansArr:
            ans += int(temp);
        return ans;
