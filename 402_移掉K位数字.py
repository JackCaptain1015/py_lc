class Solution:
    '''
    贪心+栈，要使数最小，其实就是使数从左边起单调递增，所以只要删掉左边起
    不符合单调递增的数就可以了，这里要注意的使while循环，因为前面可能有
    2个数符合，但是突然来了一个数比他们都小，那么这两个数都要删除。
    如果到最后都是单调递增了且还没删完，那么就截断尾部。
    最后的"".join(ansArr).lstrip("0") or "0"是简化的三元表达式，
    意思是如果前面是空字符串，就返回"0"
    '''
    def removeKdigits(self, num: str, k: int) -> str:
        ansArr = [];
        for c in num:
            while k > 0 and ansArr and ansArr[-1] > c:
                ansArr.pop();
                k -= 1;
            ansArr.append(c);
        ansArr = ansArr[:-k] if k>0 else ansArr;
        return "".join(ansArr).lstrip("0") or "0";

