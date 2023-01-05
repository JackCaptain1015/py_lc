class Solution:
    '''思路就是先分别计算出位置i的两边最大高度，然后取其中最小值减去i位置的高度'''
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0;
        n = len(height);
        #这里表示leftMax的第一个元素高度即height[0]，并且初始化数组剩余元素。
        #leftMax表示i在当前位置时，当前位置+左边所有位置的最大高度，因此下面
        #max比较的是height[i]而不是height[i-1]
        leftMax = [height[0]]+[0]*(n-1);
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1],height[i]);
        rightMax = [0]*(n-1)+[height[n-1]];
        for i in range(n-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],height[i]);
        ans = 0;
        for i in range(0,n):
            ans += min(leftMax[i],rightMax[i]) - height[i];
        return ans;