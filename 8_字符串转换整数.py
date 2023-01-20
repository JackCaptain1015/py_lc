import re


class Solution:
    '''
    注意，题目中要求必须是正负整数开头的字符串，否则不满足，所以正则中
    必须要有^，表示从开头匹配。最后ans = int(*arr)，因为arr如果找到的话
    实际只有一个数字，例如[123],所以*arr解包后变成123.这里如果用arr[0]的话，
    还要判断一下arr是否存在。而*arr解包,int(*arr)直接返回0（题目要求）
    '''
    def myAtoi(self, s: str) -> int:
        intMax,intMin = 2**31-1,-2**31;
        s = s.lstrip();
        reCom = re.compile(r'^[\+\-]?\d+');
        arr = reCom.findall(s);
        ans = int(*arr)
        if ans > intMax:
            return intMax;
        if ans < intMin:
            return intMin;
        return ans;