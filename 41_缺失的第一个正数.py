from typing import List

class Solution:
    '''
    原地哈希，指的是将数组数据值映射到数组对应下标的方式。
    该题中，正数只有两种可能，即正数<=size或者正数等于size+1。
    因此把<=0的值全变为size+1，防止非正数的影响。
    然后进行原地哈希，这里注意要用绝对值，因为遍历是往后进行的，如果一开始
    就把后面的值随便填成-1，那么遍历到后面时候就没办法对该值进行哈希映射了。
    最后答案为第一个出现正数的下标+1（因为有映射的都是符合<=size的正数，没有映射的
    都是缺失的，此时找第一个没有映射的，就是该位置进行缺失的值），或者
    整体都是连续的那么就是size+1
    '''
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums);
        for i in range(size):
            if nums[i] <= 0:
                nums[i] = size+1;
        for i in range(size):
            num = abs(nums[i]);
            if num <= size:
                nums[num-1] = -abs(nums[num-1]);
        for i in range(size):
            if nums[i] > 0:
                return i+1;
        return size+1;
