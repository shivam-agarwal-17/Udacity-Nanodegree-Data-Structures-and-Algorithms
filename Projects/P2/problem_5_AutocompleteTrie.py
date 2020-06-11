## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this TrieNode
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this TrieNode 
        self.children[char] = TrieNode()
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None # node corresponding to prefix does not exits in this Trie
            current_node = current_node.children[char]
            
        return current_node

class TrieNode:
    def __init__(self):
        ## Initialize this TrieNode
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this TrieNode 
        self.children[char] = TrieNode()
        
    def suffixes(self):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        
        suffix_list = []
        if self.is_word: # check if current node is the ending of a word
            suffix_list.append('')
            
        for char, child_node in self.children.items():
            child_suffix_list = child_node.suffixes()
            suffix_list.extend([char + sfx for sfx in child_suffix_list])
            
        return suffix_list
            
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

def f(prefix):
    """ Prints suffixes for input prefix. """
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

def test_autocomplete():
    print("\nTest case 1: suffixes of prefix 'a'")
    f('a')
    # nt
    # nthology
    # ntagonist
    # ntonym

    print("\nTest case 2: suffixes of prefix 'f'")
    f('f')
    # un
    # unction
    # actory

    print("\nTest case 3: suffixes of prefix 't'")
    f('t')
    # rie
    # rigger
    # rigonometry
    # ripod

    print("\nTest case 4: suffixes of prefix 'tri'")
    f('tri')
    # e
    # gger
    # gonometry
    # pod

    print("\nTest case 5: suffixes of prefix 'i'")
    f('i')
    # i not found

    print("\nTest case 6: suffixes of prefix ''")
    f('')
    # 

if __name__ == '__main__':
    test_autocomplete()