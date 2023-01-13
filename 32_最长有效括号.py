import collections


class Solution:
    '''
    两种情况入栈，"("或者栈为空的情况下为")"，
    ")"的情况下必出栈，因为如果栈内是"("则匹配，为")"的话可以直接丢弃
    （因为栈内记录的是下标（最后一个没有被匹配的右括号的下标），所以可以丢弃）。
    另外stack初始化为-1元素也很关键，这样可以在刚好匹配后使stack不为空。
    （如果一开始栈为空，第一个字符为左括号的时候我们会将其放入栈中，
    这样就不满足提及的「最后一个没有被匹配的右括号的下标」，为了保持统一，
    一开始的时候往栈中放入一个值为 -1 的元素。）
    这里计算maxLen的话，相当于每次匹配完就计算一次maxLen
    '''
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0;
        stack = [-1];
        maxLen = 0;
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i);
            else:
                stack.pop();
                if not stack:
                    stack.append(i);
                else:
                    maxLen = max(maxLen,i-stack[-1]);
        return maxLen;







