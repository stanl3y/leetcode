class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in reversed(range(len(s))):
            if s[i] != " ":
                break
        else:
            return 0

        for j in reversed(range(i+1)):
            if s[j] == " ":
                break

        return i - j + (1 if s[j] != " " else 0)
