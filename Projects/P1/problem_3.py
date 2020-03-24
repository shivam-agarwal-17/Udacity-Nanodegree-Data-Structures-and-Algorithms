import sys
from heapq import heappush, heappop

class Node:
    def __init__(self, freq=0, letter=None):
        self.freq = freq 
        self.letter = letter
        self.left = None
        self.right = None
        self.parent = None
    
    def increment_freq(self):
        self.freq += 1
    
    def is_leaf(self):
        return self.left is None and self.right is None
    
    def __repr__(self):
        return f"Node({self.freq}, {self.letter})"
    
    def __gt__(self, node):
        return self.freq > node.freq
    
    @classmethod
    def merge(cls, node_1, node_2):
        parent_node = cls(freq = (node_1.freq + node_2.freq))
        parent_node.left = node_1
        parent_node.right = node_2
        node_1.parent = parent_node
        node_2.parent = parent_node
        return parent_node

class HuffmanTree:
    def __init__(self):
        self.root = None
        self.char_to_node = dict()
        
    def _compute_char_freq(self, data):
        """ compute frequencies of characters found in the data """
        for char in data:
            if char not in self.char_to_node:
                self.char_to_node[char] = Node(freq = 1, letter = char)
            else:
                self.char_to_node[char].increment_freq()
    
    def _build_tree(self):
        """ build the Huffman tree """

        # add nodes to min-heap
        h = []        
        for _,  node in self.char_to_node.items():
            heappush(h, node)
        
        # build huffman tree
        while len(h) > 1:
            node_1 = heappop(h)
            node_2 = heappop(h)
            new_node = Node.merge(node_1, node_2)
            heappush(h, new_node)

        # get root of Huffman Tree
        self.root = heappop(h)
    
    def encode(self, data):
        """ 
        Perform Huffman encoding on data 

        Args:
            data(str): data to be Huffman encoded
        Returns:
            String of 0s and 1s denoting Huffman encoding of data 
        """

        # compute character frequencies and initialize nodes of the tree
        self._compute_char_freq(data)
        
        # building the huffman tree
        self._build_tree()
        
        # encode data
        encoded_data = ""

        if self.root.is_leaf(): # edge case: if root is also the character node, that is, only one node present in huffman tree
            for char in data:
                encoded_data += "0"
            return encoded_data
        
        for char in data:
            current_node = self.char_to_node[char]
            code = ""
            while current_node.parent is not None:
                if current_node == current_node.parent.left:
                    code += "0"
                else:
                    code += "1"
                current_node = current_node.parent
            encoded_data += code[::-1]

        return encoded_data
    
    def decode(self, data):
        """ 
        Perform Huffman decoding on data 

        Args:
            data(str): data to be Huffman decoded
        Returns:
            decoded string
        """

        current_node = self.root
        decoded_data = ""

        if self.root.is_leaf(): # edge case: if root is also the character node, that is, only one node present in huffman tree
            for char in data:
                decoded_data += self.root.letter
            return decoded_data

        for char in data:
            if char == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.is_leaf():
                decoded_data += current_node.letter
                current_node = self.root

        return decoded_data

def test_Huffman_coding(test_case_num, input_string, test_case_str):
    print(f"\nTest case {test_case_num}: {test_case_str}\n")

    HT = HuffmanTree()

    encoded_data = HT.encode(input_string)
    decoded_data = HT.decode(encoded_data)

    print ("The size of the data is: {}\n".format(sys.getsizeof(input_string)))
    print ("The content of the data is: {}\n".format(input_string))

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

if __name__ == "__main__":
    test_inputs = [("aaabbbbccd", "Input string has characters of varying frequencies"), \
                ("aabbccdd", "Input string has characters of equal frequencies"), \
                ("zzzzzzz", "Only one character present in input string")]

    for idx, test_case in enumerate(test_inputs):
        test_Huffman_coding(idx+1, test_case[0], test_case[1])
        