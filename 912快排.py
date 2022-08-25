import random


class Solution:
    def randomized_partition(self, nums, l, r):
        #基准值随机化，防止出现最坏的排序情况
        pivot = random.randint(l, r)
        #将基准值放最右边（方便下面处理）
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l;
        for j in range(l, r):
            #小于基准值的放一边(最终分界线下表就是i，因为i之前的下表都是小于基准值的)
            if nums[j] < nums[r]:
                nums[j], nums[i] = nums[i], nums[j]
                i +=1;
        #最后将基准值放到分界线位置
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomized_quicksort(self, nums, l, r):
        #partition时候最小会返回i==l的情况，即mid = l，此时如果做quicksort，
        #会出现l > r的情况，因此这时需要直接返回
        #当做快速选择时候（topK），这里不要用<=,而用<
        if r <= l:
            return
        #快排就是分区排序，把小于基准值的放一边，大于基准值的放另一边
        #每次分区都能将基准值的下标确定好，根据这种性质可以解决topK问题
        #然后递归对每个分区进行排序
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums

