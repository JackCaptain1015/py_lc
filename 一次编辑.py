#https://leetcode.cn/problems/one-away-lcci/

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        #以first为长的数组
        m, n = len(first), len(second)
        if m < n:
            return self.oneEditAway(second, first)
        if m - n > 1:
            return False
        for i, (x, y) in enumerate(zip(first, second)):
            if x != y:
                return first[i + 1:] == second[i + 1:] if m == n else first[i + 1:] == second[i:]
        return True
