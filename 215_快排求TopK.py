class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, k, 0, len(nums) - 1);

    def quickSelect(self, nums: List[int], k: int, left, right) -> int:
        if left > right:
            return -1;
        target = len(nums) - k;
        mid = self.quickPart(nums, left, right);
        if mid == target:
            return nums[mid];
        if mid > target:
            return self.quickSelect(nums, k, left, mid - 1);
        return self.quickSelect(nums, k, mid + 1, right);

    def quickPart(self, nums: List[int], left, right):
        pivot = random.randint(left, right);
        nums[pivot], nums[right] = nums[right], nums[pivot];
        i = left;
        for j in range(left, right):
            if nums[j] < nums[right]:
                nums[j], nums[i] = nums[i], nums[j];
                i += 1;
        nums[i], nums[right] = nums[right], nums[i];
        return i;




