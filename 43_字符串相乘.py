class Solution:
    '''
    这题主要是模拟乘法，不能通过把整个num通过ascii码之类的方式直接转成int然后相乘。
    因为num1*num2最大长度是size1+size2（假设num1与num2均为最大值，
    即(10^size)-1相乘，则答案长度最多为size1+size2），
    另外i,j两层循环，则是模拟num1与num2中的单个数字相乘，因为是从尾部相乘起的，所以答案也要从尾部开始存，
    并且因为num1*num2相乘过程中会有size2层数字，重合的数字层会相加，所以这里是+=。
    最后一层循环是处理进位。beginIndex是判断是否存在头部进位，如果存在就从下标0开始取，没有头部进位的话，
    那头部是默认值0，则从下标1开始取
    '''
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0";
        size1,size2 = len(num1),len(num2);
        arr = [0]*(size1+size2);
        for i in range(size1-1,-1,-1):
            for j in range(size2-1,-1,-1):
                arr[i+j+1] += int(num1[i])*int(num2[j]);
        for i in range(size1+size2-1,-1,-1):
            arr[i-1] += arr[i] // 10;
            arr[i] = arr[i] % 10;
        beginIndex = 1 if arr[0] == 0 else 0;
        return "".join([str(c) for c in arr[beginIndex:]])

