## Square Root of an Integer

### Design Choice

I saw the given problem as one of searching for floored square root of the integer, n in a sorted array from 1 to n - 1. Binary search like algorithm turned out to be a natural choice, which also ensures O(log n) worst case time complexity. 

### Time Complexity

The core function here is _sqrt_helper(), which reduces the problem size by half at every recursive call. For an integer n, there can be log n such recursive calls. Therefore, time complexity is O(log n).

### Space Complexity

We would have a function call stack for _sqrt_helper() with (log n) stack frames in the worst case. Hence, space complexity for the call stack would be O(log n).