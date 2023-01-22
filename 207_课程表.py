import collections
from typing import List


class Solution:
    '''
    拓扑排序，判断拓扑结构中是否存在环。edgeMap中key是被依赖的节点，val是依赖key的节点列表。
    numCourses就是需要遍历这么多节点(prerequisites中可能不存在这个节点，但这样就相当于没有依赖，直接就能学这个课程)，
    back函数中为节点定义了3种状态，0表示这个节点还没被搜索过，1表示这个节点的路径搜索中，2表示这个节点的路径已经搜索完了。
    这里要注意，如果一个节点下路径全部搜索完了，那么节点状态全都是2，因此换句话说，即如果A路径有个节点1，搜索完后路径状态
    是2，B路径也有节点1，这时候回进来节点状态是2，就不会进入状态为1的条件中。因此只有存在环的情况下，其路径搜索完后节点
    状态为1，所以如果搜索过程中发现依赖key的路径节点状态是1那么一定存在环。
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def back(node):
            nodeStateList[node] = 1;
            for nextNode in edgeMap[node]:
                if nodeStateList[nextNode] == 0:
                    back(nextNode);
                    continue;
                elif nodeStateList[nextNode] == 1:
                    self.ans = False;
                    return ;
            nodeStateList[node] = 2;
        edgeMap = collections.defaultdict(list);
        for tempList in prerequisites:
            edgeMap[tempList[1]].append(tempList[0]);
        nodeStateList = [0]*numCourses;
        self.ans = True;
        for nodeTemp in range(numCourses):
            if self.ans and nodeStateList[nodeTemp] == 0:
                back(nodeTemp);
        return self.ans;


print(Solution().canFinish(9,[[1,0],[2,0],[1,2]]))