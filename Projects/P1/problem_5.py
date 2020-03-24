import hashlib
from datetime import datetime
import sys

class Block:
    __slots__ = ['index', 'timestamp', 'data', 'previous_hash', 'hash', 'next'] 
    
    def __init__(self, index, timestamp, data, previous_hash):
        self.index= index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
        
    def calc_hash(self):
        """ Computes hash for the block instance """
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8'))
        sha.update(str(self.timestamp).encode('utf-8'))
        sha.update(str(self.data).encode('utf-8'))
        sha.update(str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()
    
    def __repr__(self):
        return f"Index: {self.index} \nTimestamp: {self.timestamp} \nData: {self.data} \nPrevious Hash: {self.previous_hash} \nHash: {self.hash}"

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None # added tail so don't have to traverse everytime till the end of list, we want to add a new block
        self.num_blocks = 0
        self.next_index = 0
        
    def add_block(self, data):
        """ 
        Creates a new block for data, and adds it to the block-chain 

        Args:
          data: data to be stored in the new block
        """
        if self.head is None:
            self.head = Block(self.next_index, datetime.utcnow(), data, None)
            self.tail = self.head
        else:
            self.tail.next = Block(self.next_index, datetime.utcnow(), data, self.tail.hash)
            self.tail = self.tail.next
        self.num_blocks += 1
        self.next_index += 1

    def verify_integrity(self):
        """ Verifies integrity of the block-chain """
        try:
            current_block = self.head
            while current_block.next:
                assert current_block.hash == current_block.next.previous_hash
                current_block = current_block.next
            print("\nVerifying intergrity ... Passed!")
        except AssertionError as err:
            print("\nVerifying intergrity ... Failed!")
        
    def __len__(self):
        return self.num_blocks
    
    def __iter__(self):
        current_block = self.head
        while current_block:
            yield current_block
            current_block = current_block.next
    
    def __repr__(self):
        return "\n\n".join([str(block) for block in self])
    

def test_block_chain():
    print("\nTest case 1: create a block-chain with 5 elements, print it's elements (blocks) and it's size")

    bc_1 = Blockchain()

    data_list = ["Hello", "This", "Is", "My", "BlockChain"]
    for data in data_list:
        bc_1.add_block(data)

    print(f"\nBlockChain of length {len(bc_1)}:\n\n{bc_1}")

    print("\nTest case 2: test integrity of block chain")

    bc_1.verify_integrity()

    print("\nAltering contents of block (idx 0) from 'Hello' to 'Hi'")
    bc_1.head.data = "Hi"
    bc_1.head.hash = bc_1.head.calc_hash()

    bc_1.verify_integrity()

    print("\nTest case 2: test scalability")
    data_list = range(10000)
    bc_2 = Blockchain()
    print(f"\nCreating and adding {len(data_list)} blocks to a block-chain")
    for data in data_list:
        bc_2.add_block(data)
    print(f"\nBlockchain of length {len(bc_2)} has been created!")
    bc_2.verify_integrity()

if __name__ == "__main__":
    test_block_chain()