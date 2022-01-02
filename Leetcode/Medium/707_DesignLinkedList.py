class Node():
    def __init__(self,val=0):
        self.val = val
        self.next = None

class MyLinkedList:
    """Implementation of singly linked-list. Uses class Node()."""

    def __init__(self):
        self.length = 0
        self.head = Node(0) # note: not in self.length, just a NULL placeholder
        
    def _traverse(self):
        """Internal-use method for traverseing list head to tail."""
        current = self.head
        ll = ""
        while current:
            ll += str(current.val) + " | "
            current = current.next
        if ll == "": 
            ll = "_"
        return ll
    #
    def check(method):
        """Decorator function. Uses self._traverse()"""
        def wrapper(*args):
            #print(args[0]._traverse())
            method(*args) # run the actual function called under the @decorator
            print(method.__name__,"\t",args[0]._traverse())
        return wrapper
        
        
    #@check
    def get(self, index: int) -> int:
        """Return Node.val at given index."""
        if index < 0 or index >= self.length:
            return -1 # ERROR
        else:
            current = self.head
            if current: # 
                for _ in range(index+1):
                    current = current.next
                return current.val
        
        
    #@check
    def addAtHead(self, val: int) -> None:
        """Add given value as Node() at Head."""
        return self.addAtIndex(0, val)
        
    #@check
    def addAtTail(self, val: int) -> None:
        """Add given value as Node() at Tail."""
        return self.addAtIndex(self.length, val)

    
    
    #@check
    def addAtIndex(self, index: int, val: int) -> None:
        """..."""
        #--IndexError:
        if index < 0 or index > self.length:
            return -1

        current = self.head
        
        #--Iterate to `index`:
        for _ in range(index):
            current = current.next

        #--Create the Node:
        node = Node(val)

        node.next = current.next
        current.next = node
                
        # 
        self.length += 1

    #@check
    def deleteAtIndex(self, index: int) -> None:
        """..."""
        #--IndexError:
        if index < 0 or index >= self.length:
            return -1
        
        current = self.head
        
        #--Iterate to just-before `index`:
        for _ in range(index):
            current = current.next
        
        current.next = current.next.next

        # Elem removed, reduce link length:
        self.length -= 1

      


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)






"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

  Implement the MyLinkedList class:
    MyLinkedList() Initializes the MyLinkedList object.
      int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
      void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
      void addAtTail(int val) Append a node of value val as the last element of the linked list.
      void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
      void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

  Example 1:
    Input
      ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
      [[], [1], [3], [1, 2], [1], [1], [1]]
    Output
      [null, null, null, null, 2, null, 3]

Explanation
  MyLinkedList myLinkedList = new MyLinkedList();
  myLinkedList.addAtHead(1);
  myLinkedList.addAtTail(3);
  myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
  myLinkedList.get(1);              // return 2
  myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
  myLinkedList.get(1);              // return 3
"""
