class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [] #所有不重复排列
        used = [0] * len(nums) #某数字是否已经被选
        arrangement = [0] * len(nums) #单个排列
        bitmap = [0] * 9999 #某一数字是否在同一位已经出现
        for i in range(0, len(nums)):
            if used[i] == 0 and bitmap[nums[i]] == 0:
                    used[i] = bitmap[nums[i]] = 1
                    arrangement[0] = nums[i]
                    self.dfs(1, used, ans, arrangement, nums)
                    used[i] = 0
        return ans

    def dfs(self, n, used, ans, arrangement, nums):
        if n == len(nums):
            ans.append(arrangement[:])
        else:
            bitmap = [0] * 9999 #某一数字是否在同一位已经出现
            for i in range(0, len(nums)):
                if used[i] == 0 and bitmap[nums[i]] == 0:
                    used[i] = bitmap[nums[i]] = 1
                    arrangement[n] = nums[i]
                    self.dfs(n+1, used, ans, arrangement, nums)
                    used[i] = 0

s = Solution()
print(s.permuteUnique([1,1,2]))
