# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    前序遍历+回溯，用前序遍历获取Map(这题虽然没有明说val是unique，但是实际上是unique的)，
    然后用map找到跟B相同值的节点，最后用回溯判断各个分支是否一致。
    因为B一直是小的那一方，所以回溯过程中bRoot一定会存在，如果不存在就是遍历完成了，且之前没有问题。
    '''
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def getNodeMap(root):
            if not root:
                return ;
            aMap[root.val] = root;
            getNodeMap(root.left);
            getNodeMap(root.right);
        def back(aRoot,bRoot):
            if not bRoot:
                return True;
            elif not aRoot or aRoot.val != bRoot.val:
                return False;
            return back(aRoot.left,bRoot.left) and back(aRoot.right,bRoot.right);
        if not A or not B:
            return False;
        aMap = {};
        getNodeMap(A);
        node = aMap.get(B.val);
        return back(node,B);

s = Solution()

node1 = TreeNode(10)
node2 = TreeNode(12)
node3 = TreeNode(6)
node4 = TreeNode(8)
node5 = TreeNode(3)
node6 = TreeNode(11)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6;

bnode1 = TreeNode(10)
bnode2 = TreeNode(12)
bnode3 = TreeNode(6)
bnode4 = TreeNode(8)
bnode1.left = bnode2
bnode1.right = bnode3
bnode2.left = bnode4

a = s.isSubStructure(node1,bnode1);
print(a)