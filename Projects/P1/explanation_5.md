## Block Chain

### Design Choice

As suggested in the porblem statement, I used linked-list to maintain the list of blocks contained in an instance of class Blockchain.

Other design choices:
- In class BlockChain, I maintain a tail pointer for the linked-list so insertion at tail is a constant time operation.
- In the class definition for Block, I am using __slots__ to define the class attributes, this minimizes memory occupied by the class instances by preventing the creation of attribute dictionary for every instance. This is useful if we were to create large number of class instances, which is quite possible in case a Blockchain.
- In class BlockChain, I have added a member function to verify intergrity of the block-chain, by checking if the hash of current block is same as the previous-hash stored in next block in the linked-list. Based on some reading I did, this could be useful to determine whether a block was tampered with or not, since any tampering would alter it's hash and that would cause the integrity check to fail.

### Time Complexity
- Creation of a block is O(1) as there are constant number of operations in its __init__ method. 
- Adding a new block to the block-chain is also O(1) as I am maintaing a tail pointer for the internal linked-list.

### Space Complexity
- The space complexity of the block chain should be O(N), where N is the number of blocks present in the block-chain.