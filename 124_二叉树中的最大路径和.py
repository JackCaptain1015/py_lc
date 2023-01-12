# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    整体思路是递归计算每个节点的和，这样父节点的和就是
    node.val+leftSum+rightSum，其中左右节点的效益和，最差为0，
    因为如果是负数的话，会拖累父节点的效益和，那么为0就相当于不选这条路径，
    最后返回这个节点的最大效益路径（因为对父节点来说，只能左右选其一）
    '''
    def __init__(self):
        self.maxSum = float("-inf");
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.gain(root);
        return self.maxSum;
    def gain(self,node):
        if not node:
            return 0;
        leftSum = max(self.gain(node.left),0);
        rightSum = max(self.gain(node.right),0);
        nodeSum = node.val+leftSum+rightSum;

        self.maxSum = max(nodeSum,self.maxSum);
        return node.val+max(leftSum,rightSum);


