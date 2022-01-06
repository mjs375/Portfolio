# **ALGORITHMS & DATA STRUCTURES**
---

### Linear & Binary Search
- **Linear Search**: searching an array by comparing its values 1-by-1 to the target value, usually by beginning at the left/start and advancing to the right/end until the target value is found or you can conclude it doesn't exist.
- **Binary search**: searching a sorted array by repeatedly dividing the search interval in half.
  1. Begin with an interval covering the entire array.
  2. If the target value is less than the middle item, narrow the interval to the lower half (or to the upper half is greater than).
  3. Repeat halving process until target value is found or the interval is empty.
     - Time Complexity: **O(log•n)**

---

### Linked Lists
- **(Singly) Linked Lists**: for each item in a linked list's memory is stored 1) the *current.value* and the *current.next*, or a pointer to the next item in the linked list. *Each **node** contains its item and a reference/pointer to the next item.*
  - Dynamic data structure: *no memory is reserved in advance, memory is created at run-time when a new item is added (unlike a typical `List`). Easily updateable, more flexible for implementing stacks, queues, lists...*
    - You cannot directly access a linked-list item, like `Lists`, since you only have access to the first item to start. Worst-case access time is **O(n)**.

---

### Traversal Algorithms

- **Tree Traversal**: trees are a type of graph. Also known as *checking/visiting*, or *updating* each node in a tree exactly once, without repeating any node. Because all nodes are connected via *edges/links*, start from the *root/head* (we cannot randomly access a node). Three ways:
  - **Preorder traversal** 
  - **Inorder traversal**
  - **Postorder traversal**


- **Depth-First Search (DFS)**: always explore the deepest node, that is, follow your first path as deep as possible. Once you hit a dead end (or result..) back-up and try a different path, again, all the way to its extremity. Uses a **stack**.
  - Last-in, first-out (stack) approach.

- **Breadth-First Search**:




