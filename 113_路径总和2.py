# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    '''
    深度遍历+回溯，要注意最后路径节点的弹出，尤其是答案正确时候的弹出。
    '''
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def back(node,target):
            if not node:
                return ;
            arr.append(node.val);
            target = target-node.val;
            if target == 0 and not node.left and not node.right:
                ansArr.append(arr[:]);
                arr.pop();
                return;
            back(node.left,target);
            back(node.right,target);
            arr.pop();
        ansArr = [];
        arr = [];
        back(root,targetSum)
        return ansArr;
