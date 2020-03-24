## Autocomplete with Tries

### Design Choice

There's only one main design choice I made on top of the code provided in the notebook, and that is to use Python dictionary to store the information on children of a TrieNode, this is so that we can access the trie-node by the character (or letter) it stores.

### Time Complexity

The TrieNode class has following two (non-init) methods:

1. insert():
   - this operation adds a new (key, value) pair to the Python dictionary that represents the children nodes of that partciular TrieNode, hence the time complexity of this operation is O(1).

2. suffixes():
   - this function is recursively called once for every node in the subtree rooted at that partiuclar TrieNode. In the worst case, if the words inserted in the Trie do NOT share any characters, there would be as many nodes as the characters, which is O(m), where m is the number of words inserted. Hence, the time complexity of this operation is O(m).

The Trie class has has following two (non-init) methods:

1. insert():
   - this operation iterates over the list of characters in the word which is O(n) for word of length n, and inserts the missing trie nodes using insert() of TrieNode (which is O(1)). Hence, time complexity of this operation is O(n).

2. find():
   - this method iterates over the list of characters in the word which is O(n) for word of length n, and returns the node corresponding to the last character (if it exists). Hence, time complexity for this operation is O(n).

### Space Complexity

The TrieNode class has following two (non-init) methods:

1. insert():
   - creates a new TrieNode, hence the time complexity of this operation is O(1).

2. suffixes():
   - this function is recursively called once for every node in the subtree rooted at that partiuclar TrieNode. In the worst case, if the words inserted in the Trie do NOT share any characters, there would be as many nodes as the characters, which is O(m), where m is the number of words inserted. Hence, we must have a function call stack of space complexity O(m) for this recursive operation.

The Trie class has has following two (non-init) methods:

1. insert():
   - this method has one auxiliary variable, current_node. Hence, space complexity is O(1).

2. find():
   - this method has one auxiliary variable, current_node. Hence, space complexity is O(1).

