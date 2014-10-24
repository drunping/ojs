class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A): 
        if not A: 
            return 0
        if len(A)==1:
            return A[0]
        zeroPos,minusPos=[],[]
        for pos,n in enumerate(A):
            if n==0:
                zeroPos.append(pos)
            elif n<0:
                minusPos.append(pos)
        if not zeroPos:
            if len(minusPos)%2==0:
                result=1
                for i in A:
                    result*=i
                return result
            else:
                first,last=minusPos[0],minusPos[-1]
                leftMul,rightMul=1,1
                for i in A[first+1:]:
                    leftMul*=i
                for i in A[0:last]:
                    rightMul*=i
                return max(leftMul,rightMul)
        else:
            result=0
            prePos=-1
            for pos in zeroPos:
                result=max(result,self.maxProduct(A[prePos+1:pos]))
                prePos=pos
            result=max(result,self.maxProduct(A[prePos+1:]))
            return result

s=Solution()
print s.maxProduct([0,3,0,-4])

