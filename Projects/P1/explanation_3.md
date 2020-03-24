## Huffman Coding

### Design Choice

Construction of Huffman Tree involves repeatedly querying for nodes/characters with least frequency. So, I chose to maintain a min-heap during construction of the tree, where a new node is inserted by the virtue of frequency of the character it represents. 

In order to insert nodes into min-heap, we need to be able to compare two objects of class Node, for that, I defined a custom greater-than operator, __gt__, that returns the result of comparison of their frequencies. 

For encoding, in order to ensure constant time access to the character (leaf) node in Huffman tree, I maintain a hash map from character to its corresponding (leaf) node in the tree.

### Time Complexity

#### Construction of Huffman Tree:

Steps:

1. Building dictionary or hash-map from character to the node storing it's frequency takes O(N) time, where N is the number of distinct characters found in the input string. 

2. Pushing N nodes corresponding to N distinct characters, into the min-heap takes O(NlogN) time, since height of the min-heap is O(logN).

3. Removing two of the least frequency nodes from min-heap takes O(1), merging them takes O(1) and adding the merged node into the min-heap is O(logN), and these two operations are perfromed N-1 times, so total time taken should be O(NlogN).

Total time complexity: O(NlogN)

#### Encoding

For fetching the code for each character, we need to traverse from the leaf node to the root, and then, reverse the path. This step takes O(logN) time since height of the tree is O(logN). For a string of length M, there are M characters to encode, so total time taken for encoding is O(MlogN) where M != N implies that not all characters in the input string were distinct.

#### Decoding

Decoding requires traversing as many edges of the tree as there are bits in the encoded data, so it's linear time i.e. O(M), where M denotes the number of bits in the encoded data.

### Space Complexity

1. Hash-map from N characters to corresponding nodes requires O(N) space.

2. Huffman Tree would have N leaf nodes corresponding to N characters, and roughly N-1 internal nodes, so space required is O(N) as well.

Total space complexity: O(N)
