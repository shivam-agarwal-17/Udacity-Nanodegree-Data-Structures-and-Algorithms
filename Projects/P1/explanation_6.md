## Union and Intersection

### Design Choice

Since either of the two input linked-lists could have nodes with duplicate values, I use Python set in both union() and intersection() methods, in order to ensure that the resulting linked-list doesn't have duplicate values.

- For union, I insert all elements from both linked-lists one by one to an empty set. The set by defintion would contain the union of two input lists, and set-elements are then, added to a new linked-list.

- For intersection, I maintain two sets, one to remove duplicate values from first linked-list, and second to store the intersection of two linked-lists. This is done by iterating over the values in second linked-list and checking if the value was already present in the first set. 

### Time Complexity

Assuming that the number of elements in the two input linked lists are M and N respectively.

- Union: I iterate once over all values of the two linked lists -- O(M+N), and add each value to the set -- O(1), so the total time complexity of union operation would be O(M+N). 

- Intersection: Iterating over first linked-list and adding them to a set -- O(M). Iterating over second linked-list -- O(N), searching each of its value in first set -- O(1), and adding it to a new set -- O(1). So, total time complexity of intersection operation would be O(M+N).

### Space Complexity

- Union: Worst case happens when all elements are distinct. As a result, number of elements in the union set would be M+N. So, total space complexity is O(M+N).

- Intersection: Assuming M < N, worst case hapens if all of first linked-list is contained in sencond linked-list. As a result, the number of elements in the intersection set would be M (assuming the M elements are disinct). So, total space complexity is O(M) (assuming M < N).