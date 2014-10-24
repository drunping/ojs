class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stacks=[]
        for s in tokens:
            if s=="+":
                stacks.append(stacks.pop()+stacks.pop())
            elif s=="-":
                n2,n1=stacks.pop(),stacks.pop()
                stacks.append(n1-n2)
            elif s=="*":
                stacks.append(stacks.pop()*stacks.pop())
            elif s=="/":
                n2,n1=stacks.pop(),stacks.pop()
                stacks.append(int(float(n1)/n2))
            else:
                i=int(s)
                stacks.append(i)
        return stacks.pop()

s=Solution()

t1=["2", "1", "+", "3", "*"]
t2=["4", "13", "5", "/", "+"]
t3=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print s.evalRPN(t1)
print s.evalRPN(t2)
print s.evalRPN(t3)
