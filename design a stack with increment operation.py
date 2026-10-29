class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.CustomStack=[]
        self.maxSize=maxSize

    
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.CustomStack)>=self.maxSize:
            return "Overflow"
        else:

            self.CustomStack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if(len(self.CustomStack)==0):
            return -1
        else:
            return self.CustomStack.pop()
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if (len(self.CustomStack)<k):
            for i in range(0,len(self.CustomStack)):
                self.CustomStack[i]=self.CustomStack[i]+val
        else:
            for i in range(0,k):
                self.CustomStack[i]=self.CustomStack[i]+val
        



    
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
              Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
Explanation
CustomStack stk = new CustomStack(3); // Stack is Empty []
stk.push(1);                          // stack becomes [1]
stk.push(2);                          // stack becomes [1, 2]
stk.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
stk.push(2);                          // stack becomes [1, 2]
stk.push(3);                          // stack becomes [1, 2, 3]
stk.push(4);                          // stack still [1, 2, 3], Do not add another elements as size is 4
stk.increment(5, 100);                // stack becomes [101, 102, 103]
stk.increment(2, 100);                // stack becomes [201, 202, 103]
stk.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
stk.pop();                            // return 202 --> Return top of the stack 202, stack becomes [201]
stk.pop();                            // return 201 --> Return top of the stack 201, stack becomes []
stk.pop();                            // return -1 --> Stack is empty return -1.
 


# obj.increment(k,val)
