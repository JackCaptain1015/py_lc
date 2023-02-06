class Solution:
    '''
    只有偶数个|之后才能计数
    '''
    def countAsterisks(self, s: str) -> int:
        tagCount = 0;
        ans = 0;
        for c in s:
            if c == "|":
                tagCount += 1;
                continue;
            if tagCount % 2 == 0 and c == "*":
                ans += 1;
        return ans;



