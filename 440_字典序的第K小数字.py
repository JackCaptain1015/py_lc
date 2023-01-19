class Solution:
    '''
    字典树，字典树中比如"1"，"1"的子节点可以是10~19，同理10的子节点可以是100~109.
    由此可知，字典树节点的左右移动是数字加减一来移动的，而往下层移动是通过数字乘10
    来移动的。这里prefix初始化为1，是因为答案要求的是[1,n]范围，这里1是最小的
    字典序元素，k减去该元素，所以开头k-1。而当prefix下的字典序元素个数ct小于等于
    k时，说明字典树还要往右移动，所以prefix+1，同时k减去ct个元素（因为当前元素下的
    这ct个元素都比右移后的元素小），同理，如果ct>k，说明不需要右移了，直接往下层
    移动，所以prefix*10，而k-1则是减去当前子树的根节点。
    countPrefixNodeNum中计算prefix前缀下的字典序小于n的节点个数。其中first
    根last相当于同一层下的左右指针，如果左指针小于n的话，就再往下一层。因为
    last相当于直接到下一层最右边了，所以可能会直接大于n，计算个数时候要算
    min(last,n)，而+1则是因为[1,n]是闭区间，比如13-10总共4个节点，但差值
    为3，所以要+1.
    '''
    def findKthNumber(self, n: int, k: int) -> int:
        def countPrefixNodeNum(prefix,n):
            ct,first,last = 0,prefix,prefix;
            while first <= n :
                ct = ct + min(last,n) - first +1;
                first = first*10;
                last = last*10+9;
            return ct;

        prefix = 1;
        k = k-1;
        while k:
            ct = countPrefixNodeNum(prefix,n);
            if ct <= k:
                k = k-ct;
                prefix = prefix+1;
            else:
                prefix = prefix*10;
                k = k-1;
        return prefix;
