class Solution:
    '''
    双指针，因为左右选定的情况下，因为随着宽度减小，那必然移动高度短的一方，因为
    这样才能使面积损失的更小。
    '''
    def maxArea(self, height: List[int]) -> int:
        size = len(height);
        left, right = 0, size-1;
        ans = 0;
        while right > left:
            ans = max((right-left)*min(height[right],height[left]),ans);
            if height[right] >= height[left]:
                left += 1;
            else:
                right -= 1;
        return ans;