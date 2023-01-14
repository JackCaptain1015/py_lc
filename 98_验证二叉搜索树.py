# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    注意，要验证二叉树的话，在右子树上要注意隔了几层的数依旧要大于根节点，所以不能只判断子树是否满足二叉树，
    例如[3,1,4,null,null,2,5]下4->2->5是满足二叉树的右子树的，但是2明显比根节点3小，所以不符合。
    因此这里关键是要限定要验证的左右子树的开区间，即lowVal与highVal，另外要注意相等的情况也不符合二叉树。
    最后节点不存在的情况默认返回True，不然isTree and valid下肯定为False
    '''
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node,lowVal=float('-inf'),highVal=float("inf")):
            if not node:
                return True;
            if node.val >= highVal or node.val <= lowVal:
                return False;
            isTree = valid(node.left,lowVal,node.val);
            isTree = isTree and valid(node.right,node.val,highVal);
            return isTree;
        return valid(root);
