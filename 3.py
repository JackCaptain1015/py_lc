class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {};
        left,right,res = 0,0,0;
        while right < len(s):
            c = s[right];
            if not map.get(c):
                map[c] = 0;
            map[c] = map[c] + 1;
            right = right + 1;
            while map[c] > 1:
                map[s[left]] = map[s[left]] - 1;
                left = left + 1;
            res = max(right - left,res);
        return res;


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right,maxLen = 0,0,0;
        hashmap = {};
        #窗口扩大
        while right < len(s):
            c = s[right];
            if hashmap.get(c) is None:
                hashmap[c] = 0;
            hashmap[c] += 1;
            right += 1;
            #这里不用s[right]，因为s[right]没进来，只看c的个数是不是大于1
            #窗口收缩
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
