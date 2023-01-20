# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    广度遍历，思路是为节点数与最后的节点下标一致，则说明每层节点之间没有中断，
    符合完全二叉树要求
    '''
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        arr = [(1,root)];
        nodeCount = 0;
        maxIndex = 0;
        while arr:
            tempArr = [];
            for i in range(len(arr)):
                if arr[i][1].left:
                    tempArr.append((arr[i][0]*2,arr[i][1].left));
                if arr[i][1].right:
                    tempArr.append((arr[i][0]*2+1,arr[i][1].right));
                nodeCount += 1;
                maxIndex = max(maxIndex,arr[i][0]);
            arr = tempArr;
        if nodeCount == maxIndex:
            return True;
        return False;

