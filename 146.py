class Node:
    def __init__(self,key = 0,val = 0):
        self.key = key;
        self.val = val;
        self.pre = None;
        self.next = None;

class LRUCache:

    def __init__(self, capacity: int):
        self.map = dict();
        self.head,self.tail = Node(),Node();
        #双链表操作顺畅的关键在于伪head与伪tail
        self.head.next,self.tail.pre = self.tail,self.head;
        self.capacity = capacity;
        self.size = 0;


    def get(self, key: int) -> int:
        if self.map.get(key) is None:
            return -1;
        node = self.map.get(key);
        self.moveNode(node);
        return node.val;

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key);
        if node is None:
            self.map[key] = Node(key,value);
            self.addHead(self.map[key]);
            self.size += 1;
            if self.size > self.capacity:
                delNode = self.delTail();
                self.map.pop(delNode.key);
                self.size -= 1;
            return;
        node.val = value;
        self.moveNode(node);


    #get后时间复杂度O(1)的关键在于node的直接操作，这是LRU的难点
    def moveNode(self,node:Node):
        node.pre.next = node.next;
        node.next.pre = node.pre;
        self.addHead(node);

    def addHead(self,node):
        self.head.next.pre = node;
        node.next = self.head.next;
        self.head.next = node;
        node.pre = self.head;

    def delTail(self):
        node = self.tail.pre;
        node.pre.next = self.tail;
        self.tail.pre = node.pre;
        return node;





