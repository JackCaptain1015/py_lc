class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowLen = len(grid);
        if rowLen == "0":
            return 0;
        colLen = len(grid[0]);
        islandNum = 0;
        for row in range(0,rowLen):
            for col in range(0,colLen):
                if grid[row][col] == "0":
                    continue;
                islandNum += 1;
                grid[row][col] = "0";
                deque = collections.deque([(row,col)]);
                while deque :
                    r,c = deque.popleft();
                    for x,y in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                        if 0<=x<rowLen and 0<=y<colLen and grid[x][y] == "1":
                            grid[x][y] = "0";
                            deque.append((x,y));
        return islandNum;
