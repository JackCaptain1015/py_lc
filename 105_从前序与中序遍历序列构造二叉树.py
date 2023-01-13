# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    单独的前序或中序序列是无法还原二叉树的，因为前序只能知道根节点，没法知道左右子树，
    而中序只有在知道根节点的情况下才能区分左右子树。所以两者要互相结合才能还原二叉树。
    注意，左子树个节点个数是inRootIndex-inStart，而不是inRootIndex-1，因为后续还要递归到更小的树
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preStart,preEnd,inStart,inEnd):
            if preStart > preEnd:
                return None;
            inRootIndex = inMap[preorder[preStart]];
            root = TreeNode(preorder[preStart]);
            inRootLeftNums = inRootIndex-inStart;
            root.left = build(preStart+1,preStart+inRootLeftNums,inStart,inRootIndex-1);
            root.right = build(preStart+inRootLeftNums+1,preEnd,inRootIndex+1,inEnd);
            return root;
        inMap = {val:index for index,val in enumerate(inorder)};
        return build(0,len(preorder)-1,0,len(inorder)-1);