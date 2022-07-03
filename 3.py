class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right,maxLen = 0,0,0;
        hashmap = {};
        while right < len(s):
            c = s[right];
            if hashmap.get(c) is None:
                hashmap[c] = 0;
            hashmap[c] += 1;
            right += 1;
            #这里不用s[right]，因为s[right]没进来，只看c的个数是不是大于1
            while hashmap.get(c) is not None and hashmap[c] > 1:
                #s[right]还没放进来，此时有重复了，需要left缩小
                #left缩小，就把left字符个数减掉
                hashmap[s[left]] -= 1;
                left += 1;
            maxLen = max(maxLen,right - left);
        return maxLen;

if __name__ == '__main__':
    s = Solution();
    print(s.lengthOfLongestSubstring('abcabcbb'))
