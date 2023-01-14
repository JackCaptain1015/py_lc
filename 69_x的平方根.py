class Solution:
    '''
    二分查找，注意判断边界是mid*mid<=x，且循环条件是l<=r
    '''
    def mySqrt(self, x: int) -> int:
        l,r,ans = 0,x,0;
        while l<=r:
            mid = (l+r) >> 1;
            if mid*mid <= x:
                ans = mid;
                l = mid+1;
            else:
                r = mid-1;
        return ans;
