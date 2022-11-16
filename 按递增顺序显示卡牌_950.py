'''
从a = [2, 13, 3, 11, 5, 17, 7]到b = [2, 3, 5, 7, 11, 13, 17]的步骤是:

先从a头部拿一个数出来，从尾部添加到b中；
然后从a头部拿一个数，添加到a的末尾。
先在逆转过来：

先从b尾部拿一个数，添加到a头部；
从a尾部拿一个数，添加到a头部。
所以我们一开始把数列排序好，就可以开始逆向推导了。
'''

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort();
        ans = [];
        while len(deck)>0:
            ans.insert(0,deck.pop());
            if len(deck) >0:
                ans.insert(0,ans.pop());
        return ans;