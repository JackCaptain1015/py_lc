# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    用前置遍历序列化后难点在于反序列化，这里如果用字符串的下标来做递归不好做，所以直接删除字符串数组头节点处理
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def back(node):
            if not node:
                ansArr.append("None");
                return ;
            ansArr.append(str(node.val));
            back(node.left);
            back(node.right);
        ansArr = [];
        back(root);
        return ",".join(ansArr);

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def back():
            if not dataArr :
                return None;
            if dataArr[0] == "None":
                dataArr.pop(0);
                return None;
            node = TreeNode(dataArr[0]);
            dataArr.pop(0);
            node.left = back();
            node.right = back();
            return node;
        dataArr = data.split(",");
        return back();

# print(Codec().deserialize("1,2,3,None,None,4,None,None,5,None,None"))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))