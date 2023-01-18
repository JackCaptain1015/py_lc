class Solution:
    '''
    为奇数时，中间不需要旋转，所以旋转的个数为n^2-1，即(n+1)(n-1)，偶数同理，
    因为一次循环是同时互相交换4个点，所以总的旋转次数要除以4。
    剩下就是计算旋转下标，这个可以用5X5的矩阵中的[2][0]的旋转来debug，
    例如[4][2]旋转后为[2][0]
    '''
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix);
        if size % 2 == 0:
            for row in range(size // 2):
                for col in range(size // 2):
                    matrix[row][col],matrix[size-col-1][row],\
                     matrix[size-row-1][size-col-1],matrix[col][size-row-1]\
                     = matrix[size-col-1][row],matrix[size-row-1][size-col-1],\
                    matrix[col][size-row-1],matrix[row][col]
        else:
            for row in range((size+1) // 2):
                for col in range((size-1) // 2):
                    matrix[row][col], matrix[size - col - 1][row], \
                    matrix[size - row - 1][size - col - 1], matrix[col][size - row - 1] \
                        = matrix[size - col - 1][row], matrix[size - row - 1][size - col - 1], \
                          matrix[col][size - row - 1], matrix[row][col]