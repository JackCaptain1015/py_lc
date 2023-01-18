# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    '''
    把val1限定在[1,6]，这样判断奇偶时候概率就是1/2，然后val2的范围是[1,5]，
    这样概率是1/5，所以两者相乘概率是1/10，因此如果是偶的话，那么直接返回[6,10]，
    奇的话返回[1,5]
    '''
    def rand10(self):
        """
        :rtype: int
        """
        val1,val2 = 0,0;
        while True:
            val1 = rand7();
            if val1 <= 6:
                break;
        while True:
            val2 = rand7();
            if val2 <= 5:
                break;
        if val1%2 == 0:
            return val2+5;
        return val2;
