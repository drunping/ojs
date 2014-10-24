class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s=s.strip()
        strList=s.split(" ")
        strList.reverse()
        newS=" ".join( [i.strip() for i in strList if i.strip()!=""] )
        return newS

s=Solution()
print s.reverseWords(" i  am a student ")
