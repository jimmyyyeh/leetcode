class Solution:
    """
    延續Unique Paths, 針對障礙物的位置做判斷扣除
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    # 判斷起點
                    obstacleGrid[i][j] = int(not obstacleGrid[0][0])
                elif obstacleGrid[i][j]:
                    # 當前為障礙物時
                    obstacleGrid[i][j] = 0
                else:
                    left = obstacleGrid[i][j - 1]
                    up = obstacleGrid[i - 1][j]
                    if i == 0:
                        # 只能從左邊走
                        obstacleGrid[i][j] = int(bool(left))
                    elif j == 0:
                        # 只能從上面走
                        obstacleGrid[i][j] = int(bool(up))
                    else:
                        obstacleGrid[i][j] = left + up

        return obstacleGrid[-1][-1]
