class Solution:
    """
    延續Unique Paths, 動態規劃依序累加數字即可, 當有左邊或上面可選時, 選最小的數字去累加
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    grid[i][j] = grid[i][j]
                else:
                    left = grid[i][j - 1]
                    up = grid[i - 1][j]
                    if i == 0:
                        grid[i][j] += grid[i][j - 1]
                    elif j == 0:
                        grid[i][j] += grid[i - 1][j]
                    else:
                        grid[i][j] += min(left, up)
        return grid[-1][-1]
