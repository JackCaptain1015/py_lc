import random


class Solution:
    def randomized_partition(self, nums, l, r):
        #基准值随机化，防止出现最坏的排序情况
        pivot = random.randint(l, r)
        #将基准值放最右边（方便下面处理）
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l;
        for j in range(l, r):
            #小于基准值的放一边(分界线就是nums[i])
            if nums[j] < nums[r]:
                nums[j], nums[i] = nums[i], nums[j]
                i +=1;
        #最后将基准值放到分界线位置
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomized_quicksort(self, nums, l, r):
        if r <= l:
            return
        #快排就是分区排序，把小于基准值的放一边，大于基准值的放另一边
        #然后递归对每个分区进行排序
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums

