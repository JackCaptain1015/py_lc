import collections


class Solution:
    '''
    滑动窗口，注意tSize作为需要匹配的字符串个数，且第一层循环是right in range(sSize)，
    然后记住minLen的start,end下标用于最后截断，最后收缩的情况是tSize为0，即已经
    全部匹配了，所以移动left
    '''
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return "";
        counterMap = collections.Counter(t);
        left,right = 0,0;
        sSize,tSize = len(s),len(t);
        minLen = sSize+1;
        start,end = 0,-1;
        for i in range(sSize):
            if s[i] in t:
                if counterMap[s[i]] > 0:
                    tSize -= 1;
                counterMap[s[i]] -= 1;
            while tSize == 0:
                if i-left+1 < minLen:
                    minLen = i-left+1;
                    start,end = left,i;
                if s[left] in counterMap:
                    if counterMap[s[left]] >= 0:
                        tSize += 1;
                    counterMap[s[left]] += 1;
                left += 1;
        return s[start:end+1]







