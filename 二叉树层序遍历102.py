# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #1、验证
        if root is None:
            return [];
        res = [];
        #需要一个队列，这个队列就是一层中所有的元素
        #也就是说，queue.size遍历完就是一个集合list，需要res.append(list)
        queue = [root];
        #2、遍历每层队列
        while len(queue) > 0:
            list = [];
            size = len(queue);
            for i in range(size):
                #把一层的元素全部pop出来
                node = queue.pop(0);
                list.append(node.val);
                #把pop出的元素节点往里加，作为下一次便利的前提
                if node.left is not None:
                    queue.append(node.left);
                if node.right is not None:
                    queue.append(node.right);
            res.append(list);
        return res;
