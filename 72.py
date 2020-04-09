# dfs，很多重复状态，超时

# class Solution(object):
#     def __init__(self, word1, word2):
#         self.word1 = word1
#         self.word2 = word2
#         self.map = []


#     def minDistance(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
#         return self.bfs(word1, word2)

#     def bfs(self, word1, word2):
#         # if (word1,word2) in self.map:
#         #     return 0x3f3f3f
#         # else:
#         #     self.map.append((word1, word2))
#         print(word1, word2)
#         a  = input('')
#         if word1 == word2:
#             return 0
#         elif word1 == '':
#             return len(word2)
#         elif word2 == '':
#             return len(word1)
#         elif word1[0] == word2[0]:
#             return self.bfs(word1[1:], word2[1:])
#         else:
#             return min(self.bfs(word1[1:], word2), self.bfs(word1[1:], word2[1:]), self.bfs(word1, word2[1:])) + 1
        
class Solution(object):
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2


    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        D = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            D[i][0] = i
        for j in range(n+1):
            D[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1])
                else:
                    D[i][j] = min(D[i-1][j], D[i][j-1], D[i-1][j-1]) + 1
        return D[m][n]
solution = Solution("dinitrophenylhydrazine", "acetylphenylhydrazine")
x = solution.minDistance(solution.word1, solution.word2)
print(x)