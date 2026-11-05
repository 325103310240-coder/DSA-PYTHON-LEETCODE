class Solution:
    def prec(self,c):
        if c=='^':
            return 3
        elif c=='/' or c=='*':
            return 2
        elif c=='+' or c=='-':
            return 1
        else:
            return -1
    def isrightassociative(self,c):
        return c=='^'
    def infixToPostfix(self, s):
        # code here
        
        st=[]
        res=[]
        for c in s:
            if ('a'<=c<='z' or 'A'<=c<='Z' or '0'<=c<='9'):
                res.append(c)
            elif c=='(':
                st.append(c)
            elif c==')':
                while st and st[-1]!='(':
                    res.append(st.pop())
                st.pop()
            else:
                while st and st[-1]!='(' and  \
                (self.prec(c)<self.prec(st[-1]) or (self.prec(c)==self.prec(st[-1]) and not self.isrightassociative(c))):
                    res.append(st.pop())
                st.append(c)
        while st:
            res.append(st.pop())
    
        return ''.join(res)
        
