# **ALGORITHMS & DATA STRUCTURES**

- **Sources**:
  - **Course**: [Data Structures and Algorithms](https://jovian.ai/learn/data-structures-and-algorithms-in-python) in Python, by Jovian

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
- **Linked Lists**: for each item in a linked list's memory is stored 1) the *current.value* and the *current.next*, or a pointer to the next item in the linked list.
  - Dynamic data structure: *no memory is reserved in advance, memory is created at run-time when a new item is added (unlike a typical `List`). Easily updateable, more flexible for implementing stacks, queues, lists...*
    - You cannot directly access a linked-list item, like `Lists`, since you only have access to the first item to start. Worst-case access time is **O(n)**.
