class MyQueue:
    '''
    tempArr就是用于临时存储数据，最后压回到arr中。
    '''
    def __init__(self):
        self.arr = [];
        self.tempArr = [];
        self.head = 0;

    def push(self, x: int) -> None:
        if not self.arr:
            self.head = x;
        self.arr.append(x);

    def pop(self) -> int:
        while self.arr:
            self.tempArr.append(self.arr.pop());
        popVal = self.tempArr.pop();
        if self.tempArr:
            self.head = self.tempArr[-1];
        while self.tempArr:
            self.arr.append(self.tempArr.pop());
        return popVal;

    def peek(self) -> int:
        return self.head;

    def empty(self) -> bool:
        return True if not self.arr else False;


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()