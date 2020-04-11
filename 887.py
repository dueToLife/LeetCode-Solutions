class Solution(object):
    #自底向上，超时
    def superEggDrop1(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        MAX = 10001
        D = [[MAX]*(N+1) for _ in range(K+1)]
        for i in range(K+1):
            D[i][0] = 0
        # for j in range(N+1):
        #     D[1][j] = j
        
        for i in range(1, K+1):
            for j in range(1, N+1):

                # 没有优化的DP，O(KN^2)
                # steps = []
                # max_step = 0
                # for f in range(1, j+1):
                #     max_step = max(D[i-1][f-1], D[i][j-f]) + 1
                #     steps.append(max_step)
                # D[i][j] = min(steps)
                # 用二分查找优化, O(KNlogN)
                left, right, mid = 1, j, 0
                while left + 1 < right:
                    mid = (left + right) // 2
                    if D[i-1][mid-1] < D[i][j-mid]:
                        left = mid
                    elif D[i-1][mid-1] == D[i][j-mid]:
                        right = left = mid
                        break
                    else:
                        right = mid
                D[i][j] = min(max(D[i-1][mid-1], D[i][j-mid]) for mid in range(left,right+1)) + 1
        return D[K][N]

    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        memo = {}
        def dp(k, n):
            if (k,n) not in memo:
                if n == 0:
                    ans =  0
                elif k == 1:
                    ans =  n
                else:
                    left, right = 1, n
                    while left + 1 < right:
                        mid = (left + right) // 2
                        t1 = dp(k-1, mid-1)
                        t2 = dp(k, n-mid)
                        if t1 < t2:
                            left = mid
                        elif t1 > t2:
                            right = mid
                        else:
                            right = left = mid
                    print(left,right)
                    ans = 1 + min(max(dp(k-1,mid-1), dp(k,n-mid)) 
                                    for mid in (left, right))
                memo[k,n] = ans
            return memo[k,n]
        return dp(K,N)
s = Solution()
print(s.superEggDrop(100,8191))
