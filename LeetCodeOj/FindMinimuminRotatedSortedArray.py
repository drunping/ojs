#coding:utf-8
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        s,t=0,len(num)-1
        while num[s]>num[t]:
            mid=(s+t)/2
            if num[mid]<num[t]:
                t=mid
                continue
            else:
                s=mid+1
        return num[s]

#变种二分法
iList=[1]
s=Solution()
print s.findMin(iList)
