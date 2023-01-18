class Solution:
    '''跟链表相加一个思路'''
    def addStrings(self, num1: str, num2: str) -> str:
        num1Arr = [ord(c)-ord("0") for c in num1];
        num2Arr = [ord(c)-ord("0") for c in num2];
        ansArr = [];
        hasTen = False;
        while num1Arr and num2Arr:
            val1 = num1Arr.pop();
            val2 = num2Arr.pop();
            val = val1 + val2;
            if hasTen:
                val += 1;
                hasTen = False;
            if val > 9 :
                hasTen = True;
                val -= 10;
            ansArr.append(str(val));
        while num1Arr:
            val1 = num1Arr.pop();
            val2 = 0;
            val = val1 + val2;
            if hasTen:
                val += 1;
                hasTen = False;
            if val > 9:
                hasTen = True;
                val -= 10;
            ansArr.append(str(val));
        while num2Arr:
            val1 = 0;
            val2 = num2Arr.pop();
            val = val1 + val2;
            if hasTen:
                val += 1;
                hasTen = False;
            if val > 9:
                hasTen = True;
                val -= 10;
            ansArr.append(str(val));
        if hasTen:
           ansArr.append("1");

        return "".join([ansArr[i] for i in range(len(ansArr)-1,-1,-1)]);

