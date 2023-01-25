class Solution:
    '''
    class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1, v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue=0):
            x, y = int(v1), int(v2)
            if x != y:
                return 1 if x > y else -1
        return 0

    zip_longest可以填充较小的数组，比如数组[1,2,3]与[4,5]填充为0，那么zip_longest后，就是[(1,4),(2,5),(3,0)]，
    另外这里注意int("01")会直接返回1,不需要int(lstrip("0"))
    '''
    def compareVersion(self, version1: str, version2: str) -> int:
        def compare(arr1,arr2):
            size1, size2 = len(arr1), len(arr2);
            for i in range(size1):
                if i >= size2:
                    for j in range(i, size1):
                        if arr1[j].lstrip("0"):
                            return 1;
                    return 0;
                c1, c2 = arr1[i].lstrip("0"), arr2[i].lstrip("0");
                if c1 and c2:
                    if int(c1) > int(c2):
                        return 1;
                    elif int(c1) < int(c2):
                        return -1
                    else:
                        continue;
                elif c1:
                    return 1;
                elif c2:
                    return -1;
                else:
                    continue;
            return 0;
        arr1 = version1.split(".");
        arr2 = version2.split(".");
        if len(arr1) > len(arr2):
            return compare(arr1,arr2);
        compareVal = compare(arr2,arr1);
        if compareVal == 1:
            return -1;
        elif compareVal == -1:
            return 1;
        return 0;

print(Solution().compareVersion("1.0","1.0.0"))