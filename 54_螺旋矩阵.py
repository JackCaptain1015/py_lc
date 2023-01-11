class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
            整体思路就是从左上角与右下角坐标开始，然后螺旋遍历，需要注意的就是
            left < right and top < bottom这个条件，因为最后一次遍历时候是
            left < right且top == bottom 的时候，只需要从左往右遍历
            （因为top == bottom，所以range(top+1,bottom+1)其实也不会执行）
        '''
        if not matrix or not matrix[0]:
            return [];
        rows,cols = len(matrix),len(matrix[0]);
        left,top,right,bottom = 0,0,cols-1,rows-1;
        ans = [];
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                ans.append(matrix[top][i]);
            for i in range(top+1,bottom+1):
                ans.append(matrix[i][right]);
            if left < right and top < bottom:
                for i in range(right-1,left-1,-1):
                    ans.append(matrix[bottom][i]);
                for i in range(bottom-1,top,-1):
                    ans.append(matrix[i][left]);
            left,top,right,bottom = left+1,top+1,right-1,bottom-1;
        return ans;