## Active Directory

### Design Choice

The required search problem could be solved using following approach: for the given (group, user) pair, first search if the user belongs to list of group's users, if not, recursively search for the user in the group's sub-groups. It's possible that a paricular group is a sub-group of two parent groups. In order to prevent twice exploring this group, the set of explored groups is maintained, and a group is only explored if it is not found in the set.

### Time Complexity
Assuming there are N groups (nodes) in the directory-tree rooted at input group, and assuming that a group can have a maximum of M users. Since each group is visited only once, the total time complexity for the search algorithm would be O(MN).

### Space Complexity
A function call stack is maintained for recursive calls to _is_user_in_group_helper(). Since _is_user_in_group_helper() is called for every group (node) in the directory-tree rooted at input group, and there are N such nodes, the space complexiy of the call stack would be O(N).