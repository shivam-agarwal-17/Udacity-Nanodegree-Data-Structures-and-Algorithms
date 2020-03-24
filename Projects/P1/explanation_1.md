## LRU Cache

### Design Choice

In LRU Cache, we want to maintain a list of values, and move an element to the front of this list, everytime it is accessed or set. In order to do that in constant time, I chose a doubly linked list, as removing a given node from a doubly linked list and placing it in front, just requires modifying consant number of pointers. 

However, we also want a constant time look-up (or get) functionality. To achieve that, I used a hash map (python dictionary) that stores the mapping between keys and doubly-linked-list-nodes containing the corresponding values. 

### Time Complexity

The class LRU_Cache implements two core functionalities:

- get(): This operation looks for the key in hash-table -- O(1), and if found, moves the accessed element to the front of the list -- O(1) and returns the accessed element. Hence, total time complexity of this operation is O(1)

- put(): this operation adds a (key, node) pair to the hash table -- O(1), by constructing the node to contain the value corresponding to key, and adding it in front of the internal list -- O(1). Special case:
  - If internal list has reached capacity, first, the element at the rear of list is popped -- O(1), and aforementioned process is carried out. 
  - If key is already present, this method updates the value of node against that key in hash-able, and moves the it to the front of list -- O(1)
Hence, in any case, total time complexity of this operation is O(1)

### Space Complexity

Let's assume that the capacity of our LRU Cache is N. I am storing a hash map of N (key, node) pairs -- O(N) and maintaing a doubly linked list of N nodes -- O(N). Hence, total space complexity of my implementation is O(N)