class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ''' 总的来说就是求刚好比该数组大的数组，比如[1,2,3]对应数字123，
            下一个刚好大的就是132,只是有个特殊情况，就是321后为123,因此
            这种情况需要整体反转。
            
            整体思路就是从尾部找起，找到第一个打破降序的，即nums[i]，
            然后再从尾部找起，找到第一个大于nums[i]的，即nums[j]，
            因为nums[i]打破了降序，所以降序中必然有个数比nums[i]大。
            最后交换nums[i]与nums[j]位置，然后对i后续的数进行反转
            （即降序反转为升序）
        '''
        size = len(nums);
        i = size - 2;
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1;
        if i >= 0:
            j = size - 1;
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1;
            nums[i],nums[j] = nums[j],nums[i];
        left, right = i + 1, size - 1;
        while left < right:
            nums[left], nums[right] = nums[right], nums[left];
            left += 1;
            right -= 1;
