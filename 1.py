from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            #先判断当前值的目标数是否在表中（有循环），然后将当前值加入字典
            #这是为了避免nums与自己匹配，比如6-3=3
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

if __name__ == '__main__':
    s = Solution();
    res = s.twoSum([3,2,4],6);
    print(res)
