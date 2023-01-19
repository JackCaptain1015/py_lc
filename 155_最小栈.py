class MinStack:

    '''
    辅助栈，难点主要是如何常数时间返回最小值。思路就是每次存储数据时候，就
    同时往辅助栈里存一个当前的最小值。
    '''
    def __init__(self):
        self.minVal = float("inf");
        self.arr = [];
        self.helpArr = [];

    def push(self, val: int) -> None:
        self.minVal = min(self.minVal,val);
        self.helpArr.append(self.minVal);
        self.arr.append(val);

    def pop(self) -> None:
        self.arr.pop();
        self.helpArr.pop();
        if len(self.helpArr):
            self.minVal = self.helpArr[-1];
        else:
            self.minVal = float("inf");

    def top(self) -> int:
        return self.arr[-1];

    def getMin(self) -> int:
        return self.minVal;


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()