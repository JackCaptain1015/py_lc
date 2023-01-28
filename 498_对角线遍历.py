class Solution:
    '''
    对角线一共有rows+cols-1条，偶数时从下往上遍历，奇数时从上往下遍历。
    '''
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows,cols = len(mat),len(mat[0]);
        ansArr = [];
        for i in range(rows+cols-1):
            if i % 2 == 1:
                row = 0 if i < cols else i-cols+1;
                col = i if i < cols else cols-1;
                while row < rows and col >= 0:
                    ansArr.append(mat[row][col]);
                    row += 1;
                    col -= 1;
            elif i % 2 == 0:
                row = i if i < rows else rows-1;
                col = 0 if i < rows else i-rows+1;
                while row >= 0 and col < cols:
                    ansArr.append(mat[row][col]);
                    row -= 1;
                    col += 1;
        return ansArr;