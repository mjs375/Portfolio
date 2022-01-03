class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        """Pushes elem onto stack"""
        self.stack.append(val)

    def pop(self) -> None:
        """Removes elem from top of stack"""
        self.stack.pop()

    def top(self) -> int:
        """Gets elem on top of stack"""
        return self.stack[-1]

    def getMin(self) -> int:
        """Gets minimum elem in stack"""
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:

  MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
 

Example 1:
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

"""
