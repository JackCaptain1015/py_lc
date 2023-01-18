from typing import List


class Solution:
    '''
    二分，k表示第k个元素。要找中位数，思路拆分成奇偶，如果求第一个数的话，
    那么两个数组中最小的数就是答案，思路扩展到两个数组中位数也是一样。
    这里通过k的变小而index的变大，其中index=newIndex+1其实就相当于mid+1。
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        def getMidNum(k):
            index1, index2 = 0, 0
            while True:
                #如果nums1的指针到了末尾，就返回nums2的第K个数
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                #如果k是1，就返回两个数组的当前指针对应的最小的数
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                #新的指针位置为index+k//2 - 1(因为有两个数组，所以k//2)，
                # 为了不越界需要取长度之内的最小值
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                val1, val2 = nums1[newIndex1], nums2[newIndex2]
                #新指针上较小的值的数组会放弃该数组之前的元素（包括当前指针元素，所以要+1）
                #（因为第K小的值中K即排序数组中的指针）
                if val1 <= val2:
                    #nexIndex-index+1即放弃的元素个数
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        totalLength = m + n
        #区分奇偶
        if totalLength % 2 == 1:

            return getMidNum((totalLength + 1) // 2)
        else:
            return (getMidNum(totalLength // 2) + getMidNum(totalLength // 2 + 1)) / 2

s = Solution();
s.findMedianSortedArrays([1,2],[3]);