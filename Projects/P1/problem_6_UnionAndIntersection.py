class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __repr__(self):
        return ' -> '.join([str(node) for node in self])

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def size(self):
        size = 0
        for node in self:
            size += 1

        return size

def union(llist_1, llist_2):
    """ 
    Evaluates the union of two linked lists.
    
    Args:
        llist_1(class:LinkedList): list 1
        llist_2(class:LinkedList): list 2
    Returns:
        linked list containing union of elements found in list 1 and list 2
    """
    llist_union = LinkedList()
    set_union = set()
    
    for node in llist_1:
        if node.value in set_union:
            continue
            
        set_union.add(node.value)
        llist_union.append(node.value)
       
    for node in llist_2:
        if node.value in set_union:
            continue
            
        set_union.add(node.value)
        llist_union.append(node.value)
    
    return llist_union

def intersection(llist_1, llist_2):
    """ 
    Evaluates the intersection of two linked lists.
    
    Args:
        llist_1(class:LinkedList): list 1
        llist_2(class:LinkedList): list 2
    Returns:
        linked list containing intersection of elements found in list 1 and list 2
    """

    llist_intersection = LinkedList()
    set_helper_1 = set()
    set_helper_2 = set()
    
    for node in llist_1:  
        set_helper_1.add(node.value)
       
    for node in llist_2:
        if node.value in set_helper_1 and node.value not in set_helper_2:
            set_helper_2.add(node.value)
            llist_intersection.append(node.value)
            
    return llist_intersection

def test_union_and_intersection():
    print("\nTest case 1: the two lists have some elements in common")

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(f"\nList 1: {linked_list_1}")
    print(f"\nList 2: {linked_list_2}")
    print(f"\nUnion: {union(linked_list_1,linked_list_2)}")
    print(f"\nIntersection: {intersection(linked_list_1,linked_list_2)}")

    print("\nTest case 2: the two lists have NO elements in common")

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(f"\nList 1: {linked_list_3}")
    print(f"\nList 2: {linked_list_4}")
    print(f"\nUnion: {union(linked_list_3,linked_list_4)}")
    print(f"\nIntersection: {intersection(linked_list_3,linked_list_4)}")

    print("\nTest case 3: first list is completely contained in the second list")

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [32,4,11,6]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print(f"\nList 1: {linked_list_5}")
    print(f"\nList 2: {linked_list_6}")
    print(f"\nUnion: {union(linked_list_5,linked_list_6)}")
    print(f"\nIntersection: {intersection(linked_list_5,linked_list_6)}")

    print("\nTest case 4: first list is empty")

    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = []
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_7.append(i)

    for i in element_2:
        linked_list_8.append(i)

    print(f"\nList 1: {linked_list_7}")
    print(f"\nList 2: {linked_list_8}")
    print(f"\nUnion: {union(linked_list_7,linked_list_8)}")
    print(f"\nIntersection: {intersection(linked_list_7,linked_list_8)}")

if __name__ == "__main__":
    test_union_and_intersection()