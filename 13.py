class Solution(object):
    def __init__(self,k):
        self.k = k

    def count(self, n):
        m = 0
        while n:
            m += n % 10
            n = n // 10
        return m

    def dfs(self, i, j, k):
        self.board[i][j] = 1
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for d in range(4):
            x = i + dx[d]
            y = j + dy[d]
            if x < 0 or y < 0 or x >= self.m or y >= self.n:
                continue
            elif self.board[x][y] == 0 and self.count(x) + self.count(y) <= k:
                self.dfs(x, y, k)
            
            
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        self.m = m
        self.n = n
        self.board = [[0]*n for _ in range(m)]
        self.dfs(i, j, k)
        result = 0
        for i in range(m):
            for j in range(n):
                if self.board[i][j] == 1:
                    result += 1
        return result

s = Solution(8)
k = s.movingCount(3, 1 ,0)
print(k)