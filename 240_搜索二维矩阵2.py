from typing import List


class Solution:
    '''
    排除一些不符合条件的行，然后直接二分按行查找
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0]);
        for i in range(rows):
            left, right = 0, cols - 1;
            if matrix[i][-1] < target or matrix[i][0] > target:
                continue;
            while left <= right:
                mid = (left+right) // 2;
                if matrix[i][mid] == target:
                    return True;
                if matrix[i][mid] < target:
                    left = mid+1;
                    continue;
                if matrix[i][mid] > target:
                    right = mid-1;
                    continue;
        return False;

s = Solution();
a = s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5)
print(a)