#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, value, key=None):
        self.value = value
        self.key = key 
        self.prev = None
        self.next = None
        
    def __repr__(self):
        return f'Node({self.value})'

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def prepend(self, new_node):
        """ 
        Prepends a new node at the head of the list 

        Args:
            new_node(class:Node): new node to be prepended to the list
        """
        if self.head is None: 
            self.head = new_node
            self.tail = self.head
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def pop(self):
        """ Pops the tail node of the list, and returns it's key """
        if self.head is None: # list is empty
            return 
        
        popped_key = self.tail.key
        self.tail = self.tail.prev
        self.tail.next = None
        return popped_key

    def remove(self, node):
        """ 
        Remove a node from the list 

        Args:
            node(class:Node): node to be removed from the list
        """
        if self.head is None: # list is empty
            return 
        
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            
            
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
        
    def __repr__(self):
        node_list_str = ','.join([str(node) for node in self])
        return f"DoublyLinkedList({node_list_str})"

class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.num_elements = 0
        self.table = {} # hash table for storing (key, dll-node) pairs.
        self.list = DoublyLinkedList()

    def get(self, key):
        """ 
        Retrieve value corresponding to key 

        Args:
            key: query key
        Returns:
            value corresponding to query key. If key not found, returns -1
        """
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.table:
            return -1
        
        accessed = self.table[key]
        self.list.remove(accessed)
        self.list.prepend(accessed)
        return accessed.value

    def set(self, key, value):
        """ 
        Set the value corresponding to a key in the cache. If the cache is at capacity, removes the oldest item.     

        Args:
            key: key to be set
            value: value to be set against key
        """
        # 
        if key not in self.table:
            if self.num_elements == self.capacity:
                popped = self.list.pop()
                del self.table[popped]
                self.num_elements -= 1
                
            self.table[key] = Node(value, key)
            self.list.prepend(self.table[key])
            self.num_elements += 1
        else: # if key present, update the value and move it in front of the list
            updated = self.table[key]
            updated.value = value
            self.list.remove(updated)
            self.list.prepend(updated)

def test_LRU_Cache():

    print("\nInitializing LRU cache of capacity 5\n")
    our_cache = LRU_Cache(5) 

    # inserting (key, value) pairs
    data = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    for key, value in data:
        our_cache.set(key, value)
        print(f"Set {key}: {value}")

    print("\nTest case 1: attempt to get a valid key")
    print(f"Get 1: {our_cache.get(1)}")
    # Get 1: 1

    print("\nTest case 2: attempt to get an invalid key")
    print(f"Get 6: {our_cache.get(6)}")
    # Get 6: -1

    print("\nTest case 3: insert beyond capacity and attempt to get the least used key")
    our_cache.set(7, 7)
    print("Set 7:7")
    print(f"Get 2: {our_cache.get(2)}")
    # Get 2: -1   

    print("\nTest case 4: update value for existing key")
    our_cache.set(1, 10)
    print("Set 1:10")
    print(f"Get 1: {our_cache.get(1)}")
    # Get 1: 10

if __name__ == "__main__":
    test_LRU_Cache()


