# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    广度遍历，广度与深度的区别在于广度是列表+循环，而深度是递归。
    广度要注意的是第二层循环中，tempArr是一层数据，所以要用循环，
    最后整层数据替换root这一层数据。
    这题求宽度，[root,1]中1表示的是节点下标从1开始计算，所以最后
    宽度就是每层中的最大值，即最右下标减去最左下标+1.
    '''
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0;
        arr = [[root,1]]
        while arr:
            tempArr = [];
            for node,i in arr:
                if node.left:
                    tempArr.append([node.left,2*i]);
                if node.right:
                    tempArr.append([node.right,2*i+1]);
            ans = max(ans,arr[-1][1] - arr[0][1]+1);
            arr = tempArr;
        return ans;
