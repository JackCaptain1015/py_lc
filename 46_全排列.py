class Solution:
    '''
        把数组的全排序想象成一棵树，叶子节点就是所有情况，
        那么first==size的情况就是一条分支上走到底的情况，
        而back递归就是该分支往下走，随着递归的回归，顺便把swap
        交换回来，就是回溯的过程。for i in range(first,size)中i就是
        代表各个分支。数组是在初始数组上交换数据的形式来实现排列的，最终到
        叶子节点后append到ansArr中，然后回溯到最初状态开始走另一条分支。
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums);
        ansArr = [];
        self.back(nums,size,0,ansArr);
        return ansArr;

    def back(self,nums:List[int],size,first,ansArr:List[List[int]]):
        if first == size:
            ansArr.append(nums[:]);
        for i in range(first,size):
            nums[first],nums[i] = nums[i],nums[first];
            self.back(nums,size,first+1,ansArr);
            nums[first], nums[i] = nums[i], nums[first];


