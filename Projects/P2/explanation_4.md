## Dutch National Flag Problem

### Design Choice
The requirement of the problem is to sort the array of 0s, 1s and 2s in a single traversal. For this I maintain three indices, left_index which denotes the next available index to hold a 0, mid_index that denotes the next available index to hold a 1, and right_index that denotes the next available index to hold a 2. 

### Time Complexity
The inputs array gets sorted in a single traversal, hence, the time complexity is O(n), where n is the number of elements in input array.

### Space Complexity
The input array gets sorted in-place, and constant number (three) of auxiliary variables are used: left_index, mid_index and right_index. Therefore, the space xomplexity is O(1).