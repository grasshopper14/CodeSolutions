class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        i=0
        j=0
        tp = 0
        pp = -1
        while i<n:
            if j<m and s[i]==p[j] or j<m and p[j]=='?':
                i+=1
                j+=1
            elif j<m and p[j] == '*':
                tp = i
                pp = j
                j+=1
            elif pp>=0:
                j = pp+1 
                i = tp+1 
                tp+=1
            else:
                return False
        while j<m and p[j]=='*':
            j+=1
        return j==m
