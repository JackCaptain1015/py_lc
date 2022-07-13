class Solution:
    def isValid(self, s: str) -> bool:
        list = [];
        lastChar = None;
        for c in s:
            if (lastChar == "(" and c == ")") or (lastChar == "[" and c == "]") or (lastChar == "{" and c == "}"):
                list.pop();
                lastChar = None if len(list) == 0 else list[-1];
                continue;
            list.append(c);
            lastChar = c;
        return True if len(list) == 0 else False;
