class Solution:
    '''
    辅助栈，栈是二维的，栈中存储的是下一次的循环次数与之前的答案（因为在遇到"["后就存储了ansStr然后又清空了ansStr）
    '''
    def decodeString(self, s: str) -> str:
        arr, ansStr, loopNum = [], "", 0
        for c in s:
            if c == '[':
                arr.append([loopNum, ansStr])
                ansStr, loopNum = "", 0
            elif c == ']':
                tempNum, beforeAns = arr.pop()
                ansStr = beforeAns + tempNum * ansStr
            elif '0' <= c <= '9':
                loopNum = loopNum * 10 + int(c)
            else:
                ansStr += c
        return ansStr

s = Solution()
a = s.decodeString("3[a]2[bc]");
print(a)
