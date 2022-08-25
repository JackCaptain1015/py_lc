# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return [];
        queue = [root];
        res = [];
        hasLeft = True;
        while len(queue) > 0:
            list = [];
            size = len(queue);
            for i in range(size):
                node = queue.pop(0);
                if hasLeft:
                    list.append(node.val);
                else:
                    list.insert(0,node.val);
                if node.left is not None:
                    queue.append(node.left);
                if node .right is not None:
                    queue.append(node.right);
            res.append(list);
            hasLeft = not hasLeft;
        return res;