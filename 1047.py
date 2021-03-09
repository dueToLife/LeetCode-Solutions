class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) <= 1:
            return S
        flag = True
        while flag and len(S)>1:
            flag = False
            for i in range(len(S)-1):
                if S[i] == S[i+1]:
                    S = self.removeSingleLetter(S, i)
                    flag = True
                    break
        return S

    def removeSingleLetter(self, s, index):
        return s[:index]+s[index+2:]

test = Solution()
print(test.removeDuplicates("absdafbaasdfca"))
