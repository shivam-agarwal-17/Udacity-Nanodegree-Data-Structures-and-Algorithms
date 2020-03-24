## Unsorted Integer Array

### Design Choice
In order to find max and min in a single traversal, I just maintained two auxiliary variables _min and _max, both were intialized to the first element in the unsorted array. Thw teo elements are updated as required, while traversing through the array.

### Time Complexity
get_min_max() computes the min and max in a singe traversal, hence, the time complexity of this method is O(n).

### Space Complexity
Only two auxiliary variables are required to track min and max in get_min_max(), hence, the space complexity is O(1).