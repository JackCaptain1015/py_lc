class Solution:
    def getPalindromeIndex(self,s:str,left,right):
            while 0<=left and right < len(s) and left <= right and s[left] == s[right]:
                left -= 1;
                right += 1;
            return left+1,right-1;

    def longestPalindrome(self, s: str) -> str:
        start,end = 0,0;
        for i in range(len(s)):
            l1,r1 = self.getPalindromeIndex(s,i,i);
            l2,r2 = self.getPalindromeIndex(s,i,i+1);
            if r1 - l1 > end - start:
                start,end = l1,r1;
            if r2 - l2 > end - start:
                start,end = l2,r2;
        return s[start:end+1];
