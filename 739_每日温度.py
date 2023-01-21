from typing import List


class Solution:
    '''
    栈，栈中存储的是元素的下标，然后判断当前温度是否大于栈顶下标所对应的温度，如果大于就
    弹出并记录答案。这样就能做到右边较大的值与左边多个较小的值做临近匹配。
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures);
        ansArr = [0]*size;
        tempArr = [];
        for i in range(size):
            while tempArr and temperatures[i] > temperatures[tempArr[-1]]:
                ansArr[tempArr[-1]] = i-tempArr[-1];
                tempArr.pop();
            tempArr.append(i);
        return ansArr;
print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))