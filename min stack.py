class MinStack(object):

    def __init__(self):
        self.MinStack=[]
        self.minstack=[]
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.MinStack.append(value)
        if (len(self.minstack)==0):
            self.minstack.append(value)
        else:
            self.minstack.append(min(value,self.minstack[-1]))
        

    def pop(self):
        """
        :rtype: None
        """
        if(len(self.MinStack)==0):
            return "Underflow"
        else:
            self.MinStack.pop()
            self.minstack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.MinStack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
      Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 


# param_4 = obj.getMin()
