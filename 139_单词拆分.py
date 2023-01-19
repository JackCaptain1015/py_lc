from typing import List


class Solution:
    '''
    动规，转移方程是dp[i]=dp[j] and isExist(s[j:i])，其中i表示第i个字符，
    第0个表示空串，最后返回最后一个字符匹配的情况，即dp[-1]
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordMap = {val:val for val in wordDict};
        boolArr = [False]*(len(s)+1);
        boolArr[0] = True;
        for i in range(1,len(s)+1):
            for j in range(i):
                if boolArr[j] and wordMap.get(s[j:i]):
                    boolArr[i] = True;
                    break;
        return boolArr[-1];

s = Solution();
a = s.wordBreak("leetcode",["leet","code"]);
print(a)
