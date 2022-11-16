class Solution:
    def numSquares(self, n: int) -> int:
        ansList = [0]*(n+1);
        for i in range(1,n+1):
            minVal = sys.maxsize;
            for j in range(1,i+1):
                if j*j > i:
                    break;
                #ansList[i-j*j]的意思就是到j时候所需要的完全平方数，那还需要i-j*j大小的最小完全平方数
                minVal = min(minVal,ansList[i-j*j]);
            ansList.insert(i,minVal+1);
        return ansList[n];
