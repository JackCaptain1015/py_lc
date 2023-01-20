class Solution:
    '''
    两次遍历，可以把“相邻两个孩子评分更高的孩子会获得更多的糖果”条件
    拆为从左往右与从右往左两个规则，然后取其中在这个孩子身上的能拿到糖果的最大值，
    最后相加得到最少需要的总糖果数
    '''
    def candy(self, ratings: List[int]) -> int:
        size = len(ratings);
        arr = [0]*size;
        for i in range(size):
            if i > 0 and ratings[i-1] < ratings[i]:
                arr[i] = arr[i-1]+1;
            else:
                arr[i] = 1;
        rightCount = 0;
        for i in range(size-1,-1,-1):
            if i < size-1 and ratings[i] > ratings[i+1]:
                rightCount += 1;
            else:
                rightCount = 1;
            arr[i] = max(rightCount,arr[i]);
        return sum(arr);