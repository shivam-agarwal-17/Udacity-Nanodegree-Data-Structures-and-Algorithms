# A RouteTrieNode
class RouteTrieNode:

    def __init__(self, handler=None):
        """ Initialize the node with children and a handler """

        self.children = {}
        self.handler = handler

    def insert(self, path_segment):
        """ Insert a new node, which represents a segment of the split path """

        self.children[path_segment] = RouteTrieNode()

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:

    def __init__(self, handler=None):
        """ Initialize the trie with an root node and a handler """

        self.root = RouteTrieNode(handler)

    def insert(self, list_path_segments, handler):
        """ Insert (split )path and corresponding handler """

        current_node = self.root
        for segment in list_path_segments:
            if segment not in current_node.children:
                current_node.insert(segment)
            current_node = current_node.children[segment]

        current_node.handler = handler

    def find(self, list_path_segments):
        """ Return the handler for (split) path supplied, or None if no match found"""

        current_node = self.root
        for segment in list_path_segments:
            if segment not in current_node.children:
                return None
            current_node = current_node.children[segment]

        return current_node.handler 

# The Router class will wrap the Trie and handle 
class Router:

    def __init__(self, root_handler=None, not_found_handler=None):
        """ Create a new RouteTrie for holding our routes """

        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        """ Add a handler for a path """

        self.trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        """ lookup path (by parts) and return the associated handler """

        search = self.trie.find(self.split_path(path))
        if search is None:
            search = self.not_found_handler

        return search

    def split_path(self, path):
        """ split the path into parts """

        path_split = path.split('/')

        if path_split[0] == '':
            path_split.pop(0)
        if path_split[-1] == '':
            path_split.pop(-1)

        return path_split

def test_router():

    # create the router and add a route
    print("\nInitializing a Router with 'root handler' and 'not found handler'")
    router = Router("root handler", "not found handler") 

    print("\nAdding handler for URL, '/home/about': 'about handler'")
    router.add_handler("/home/about", "about handler")  

    print("\nTest case 1: look-up handler for '/'")
    print(router.lookup("/"))
    # root handler

    print("\nTest case 2: look-up handler for '/home'")
    print(router.lookup("/home"))
    # not found handler

    print("\nTest case 3: look-up handler for '/home/about'")
    print(router.lookup("/home/about"))
    # 'about handler'

    print("\nTest case 4: look-up handler for '/home/about/'")
    print(router.lookup("/home/about/"))
    # 'about handler'

    print("\nTest case 5: look-up handler for '/home/about/me'")
    print(router.lookup("/home/about/me"))
    # 'not found handler'

if __name__ == "__main__":
    test_router()