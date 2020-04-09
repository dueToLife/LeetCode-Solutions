class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        self.right = 0
        self.left = 1
        self.dfs('(', n)
        return self.ans

        
    def dfs(self, par, n):
        if self.right == n:
            self.ans.append(par)
        else:
            if self.left < n:
                self.left += 1
                self.dfs(par+'(', n)
                self.left -= 1
            if self.left > self.right:
                self.right += 1
                self.dfs(par+')', n)
                self.right -= 1

s = Solution()
print(s.generateParenthesis(8))

            

