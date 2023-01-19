class Solution:
    '''
    动规，arr[i][j]表示word1的前i个字符转化到word2的前i个字符所需要的最小步骤。
    其中操作步骤有三步，arr[i-1][j]+1，表示既然i-1到j只要X步，那么现在i到j只
    多了一个字符，所以只要多操作一步添加就可以了，因此要+1.arr[i][j-1]+1也是同理。
    arr[i-1][j-1]表示i-1到j-1所需步骤，这是在最后一个字符相同的情况下，如果最后
    一个字符不相同，需要多操作一步替换，所以有+1的判断。
    最后arr初始化为size+1长度，是因为边界情况需要初始化，因此后面range(1,size+1)
    的情况下，word[i-1]相当于range(0,size)下的word[i]。
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        size1,size2 = len(word1),len(word2);
        if not size1 or not size2:
            return size1+size2;
        arr = [[0]*(size2+1) for i in range(size1+1)];
        for i in range(size1+1):
            arr[i][0] = i;
        for j in range(size2+1):
            arr[0][j] = j;
        for i in range(1,size1+1):
            for j in range(1,size2+1):
                val1,val2 = arr[i-1][j]+1,arr[i][j-1]+1;
                val3 = arr[i-1][j-1];
                if word1[i-1] != word2[j-1]:
                    val3 += 1;
                arr[i][j] = min(val1,val2,val3);
        return arr[size1][size2];