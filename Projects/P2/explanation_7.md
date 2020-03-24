## Request Routing in a Web Server with a Trie

### Design Choice

The boilerplate code that came with the problem statement provided a nice structure to define classes, their methods, and fill in their functionality. Following are some design choices I made on top of the code provided:

1. uses Python dictionary to store the information on children of a RouteTrieNode, this is so that we can access the trie-node by the path-segment it stores, where path-segment is a part between two '/' in a URL path.

2. [BONUS] added the functionality to add a not found handler in the __init__() method of class Router. This handler is returned whenever the queried path is not found in the Trie.

3. [BONUS] added handling of edge cases related to trailing slashes. For example:
- a request for '/about' or '/about/' would direct to the same page.
- a request for '' or '/' would direct to the root handler. 

### Time Complexity

The Router class has following two (non-init) methods:

1. split_path():
   - splits input URL path, using Python's .split() which has time-complexity of O(n) where n is the length of the input string.

2. add_handler():
   - calls split_path() -- O(n)
   - calls insert() of class RouteTrie: this method iterates over the list of path segments which is O(n), and inserts the missing trie nodes using insert() of RouteTrieNode (which is O(1) as it's just adding a new (key, value) pair to Python dictionary).

Hence, total time complexity of add_handler() is O(n).

3. lookup():
   - calls split_path() -- O(n)
   - calls find() of class RouteTrie: this method iterates over the list of path segments which is O(n), and returns the handler corresponding to the last segment (if it exists)

Hence, total time complexity of lookup() is O(n).

### Space Complexity

The Router class has following two (non-init) methods:

1. split_path():
   - creates auxiliary list of path segments, path_split. Hence, space complexity of this method is O(n).

2. add_handler():
   - calls split_path(): this method returns the list of path segments, which is of size, O(n)
   - calls insert() of class RouteTrie: has one auxiliary variable current_node -- O(1). 

Hence, total space complexity of add_handler() is O(n).

3. lookup():
   - calls split_path(): this method returns the list of path segments, which is of size, O(n)
   - calls find() of class RouteTrie: has one auxiliary variable current_node -- O(1)

Hence, total space complexity of lookup() is O(n).

