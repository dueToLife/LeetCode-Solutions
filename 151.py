class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slists = s.split()
        slists.reverse()
        space = ' '
        return space.join(slists)