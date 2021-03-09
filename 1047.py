#方法一
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
#方法二
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for letter in S:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)

test = Solution()
print(test.removeDuplicates("absdafbaasdfca"))
