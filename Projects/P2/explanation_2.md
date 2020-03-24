## Search in a Rotated Sorted Array

### Design Choice

The exected time complexity of this problem was O(log n). Thinking along the lines of binary search approach, I chose to implement a procedure for searching the pivot in O(log n) time, and then, to carry out modified binary search (that takes into account the knowledge of this pivot), again in O(log n) time, ensuring that total time complexity is O(log n).

### Time Complexity

There are two steps:

1. Search pivot: I have defined pivot as the index of the smallest element in the input list. So, if the input list is [5, 7, 0, 2, 4], the pivot would be index of 0 i.e. 2. The core method for this is _search_pivot_helper() that reduces the problem size by half at every recursive call, by only searching for pivot in the unsorted half of the array. Since, there can be log n such recursive calls, the time complexity for this step is O(log n).

2. Search number: After finding the pivot, I used binary search with slight modification in _rotated_array_search_helper() method. The modification is that the start and end indices are shifted by pivot, and middle index is wrapped around the length of input list, using the modulo operator. Same as in binary search, the problem size is reduced by half at every step, and hence, the time complexity for this step is O(log n).

Therefore, total worst-case time complexity for above two steps is O(log n).

### Space Complexity

1. Search pivot: A call stack is maintained for recursive calls of _search_pivot_helper() with at most (log n) stack frames. Hence, this step has space complexity of O(log n).

2. Search number: A call stack is maintained for recursive calls of _rotated_array_search_helper() with at most (log n) stack frames. Hence, this step has space complexity of O(log n) as well.