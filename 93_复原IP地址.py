from typing import List


class Solution:
    '''
    回溯，回溯的参数一般都是指针并且在同一数组中通过下表进行修改。
    这里要注意根据ip地址4个分段进行回溯，并且前面处理了"0"的ip段后，要注意
    后面循环里就不能是>=0，并且回溯中段与段开始下标都要+1，如果下标没+1，那么就会
    一直重复，毕竟循环里这个i已经处理过了，下个回溯肯定不能再处理相同的值
    '''
    def restoreIpAddresses(self, s: str) -> List[str]:
        def back(segIndex,segStart):
            if segIndex == 4:
                if segStart == len(s):
                    ip = ".".join(segArr);
                    ansArr.append(ip);
                return ;
            if segStart == len(s):
                return ;
            if s[segStart] == "0":
                segArr[segIndex] = s[segStart];
                back(segIndex+1,segStart+1);
            num = 0;
            for i in range(segStart,len(s)):
                num = num*10+int(s[i]);
                if num >0 and num <= 255:
                    segArr[segIndex] = str(num);
                    back(segIndex+1,i+1);
                else:
                    break;
        ansArr = [];
        segArr = [0]*4;
        back(0,0);
        return ansArr;
