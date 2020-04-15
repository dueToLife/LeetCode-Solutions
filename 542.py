class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(matrix)
        M = len(matrix[0])
        dis = [[200]*M for _ in range(N)]
        def dfs(i, j):
            if matrix[i][j] == 0:
                dis[i][j] = 0

            for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = i + dx
                y = j + dy
                if 0 <= x < N and 0 <= y < M:
                    if matrix[x][y] == 1 and dis[i][j] + 1 < dis[x][y]:
                        dis[x][y] = dis[i][j] + 1
                        dfs(x, y)

        for i in range(N):
            for j in range (M):
                dfs(i, j)
        return dis