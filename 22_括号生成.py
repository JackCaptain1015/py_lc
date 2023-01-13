class Solution:
    '''
        回溯法，arr为一次分支的临时数组，最终有结果后放入ans，
        if left<n与if right>left就是分支，从left<n里一直走不通，
        pop后就走到right<left中。
        可以拿n=2的情况试一下流程。
    '''
    def __init__(self):
        self.ans = [];
    def generateParenthesis(self, n: int) -> List[str]:
        self.back([],n,0,0);
        return self.ans;
    def back(self,arr,n,left,right):
        if len(arr) == 2*n:
            self.ans.append("".join(arr));
            return;
        if left < n:
            arr.append("(");
            self.back(arr,n,left+1,right);
            arr.pop();
        if right < left:
            arr.append(")");
            self.back(arr,n,left,right+1);
            arr.pop();

