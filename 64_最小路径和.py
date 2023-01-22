from datetime import datetime
from typing import List


class Solution:
    '''
    动规，除了边界外，右下脚和的最小值等于临边和的最小值加当前节点。
    注意二维数组的创建只能是[[0]*cols for i in range(rows)],通过[[0]*cols]*rows
    创建出来的二维数组，里面的元素是相同的引用，也就是说，只是把里面的数组对象引用复制了rows份。
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0]);
        arr = [[0]*cols for i in range(rows)];
        arr[0][0] = grid[0][0];
        for i in range(1,rows):
            arr[i][0] = arr[i-1][0]+grid[i][0];
        for i in range(1,cols):
            arr[0][i] = arr[0][i-1] + grid[0][i];
        for i in range(1,rows):
            for j in range(1,cols):
                arr[i][j] = min(arr[i][j-1],arr[i-1][j])+grid[i][j];
        return arr[rows-1][cols-1];


print(datetime.now())
print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(datetime.now())
