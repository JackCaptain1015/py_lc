from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        def getKthElement(k):
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
                #新的指针位置为index+k//2 - 1，为了不越界需要取长度之内的最小值
                #(因为有两个数组，所以k//2)
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                #新指针的值
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                #新指针上较小的值的数组会放弃该数组之前的元素（包括当前指针元素，所以要+1）
                #（因为第K小的值中K即排序数组中的指针）
                if pivot1 <= pivot2:
                    #nexIndex-index+1即放弃的元素个数
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        totalLength = m + n
        #区分奇偶
        if totalLength % 2 == 1:
            #totalLength+1 // 2即第K个最小数，因为指针是0开始的，所以要+1
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


if __name__ == '__main__':
    s = Solution();
    nums1 = [1,3];
    nums2 = [2]
    num = s.findMedianSortedArrays(nums1,nums2);
    print(num)