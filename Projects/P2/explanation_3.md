## Rearrange Array Digits

### Design Choice
I decided to first sort the input list in-place using heapsort, and then, construct two numbers using alternate digits in the input list. For example, if the input list is of size 5, digits at index 0, 2, 4 form first number, and digits at index 1, 3 form the second number.

### Time Complexity
There are two steps:

1. Heapsort: It has two steps: build_heap() which has a time complexity of O(n), and down_heapify() for n elements, which has a time complexity of O(nlogn), hence, total time complexity for heapsort is O(nlogn).

2. Calcualte two nubers: this requires iterating over the sorted input list once, hence, it's complexity is O(n)

Therefore, total time complexity for above two steps is O(nlogn).

### Space Complexity

Since heapsort is in-place, it doesn't add to space complexity. We do have a function call stack for the recursive calls to down_heapify(). Since down_heapify() is called at max O(log n) times, the space complexity of the call stack would be O(log n).
