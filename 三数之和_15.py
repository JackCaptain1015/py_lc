class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #1、验证数组大小
        n = len(nums)
        if (not nums or n < 3):
            return []
        #2、排序
        nums.sort()
        res = []
        #3、遍历
        for i in range(n):
            #遍历到正数后就退出
            if (nums[i] > 0):
                return res
            #如果两个值一样就跳过
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            #双指针
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res

