# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
         使用深度优先搜索，整体思路就是使用栈后进先出，使每次遍历都是最新走右节点，
         然后使用dict的setdefault，使如果这层放过最右节点了，就不再放置，最后遍历dict输出结果
        '''
        map = dict();
        maxDepth = -1;
        stack = [(root,0)];
        while stack:
            node,depth = stack.pop();
            '''注意这里要判断node是否存在，因为root也是Optional'''
            if node:
                maxDepth = max(depth,maxDepth);
                map.setdefault(depth,node.val);
                depth += 1;
                stack.append((node.left,depth));
                stack.append((node.right,depth));
        return [map[depth] for depth in range(maxDepth+1)];
