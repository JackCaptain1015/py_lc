from typing import List


class Solution:
    '''
    回溯，整体思路很简单，就是二维数组中每个字符的上下左右都判断一遍，如果存在字符相符就继续递归。
    注意的点就是需要字典存储在当前字符上已经访问过的坐标，且在递归中需要回溯。
    定义enumList中来确定上下左右需要加减的坐标，可以使回溯更简单，使多次递归调用变成了循环中调用递归。
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        def back(row,col,i):
            if board[row][col] != word[i]:
                return False;
            if i == len(word)-1:
                return True;
            existIndexMap[(row,col)]=1;
            result = False;
            for ei,ej in enumList:
                tempRow,tempCol = row+ei,col+ej;
                if 0 <= tempRow < len(board) and 0 <= tempCol < len(board[0]):
                    if (tempRow,tempCol) not in existIndexMap:
                        if back(tempRow,tempCol,i+1):
                            result = True;
                            break;
            existIndexMap.pop((row,col));
            return result;
        existIndexMap = {}
        enumList = [(0,1),(0,-1),(1,0),(-1,0)];
        rows,cols = len(board),len(board[0]);
        for row in range(rows):
            for col in range(cols):
                if back(row,col,0):
                    return True;
        return False;
