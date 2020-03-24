def down_heapify(arr, n, index):
    """
    Performs down heapify operation on node at index, i of the array, arr containing n elements.
    """
    
    assert(index < n)
    
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    
    max_node_idx = index
    if left_index < n and arr[left_index] > arr[index]:
        max_node_idx = left_index
        
    if right_index < n and arr[right_index] > arr[max_node_idx]:
        max_node_idx = right_index
        
    if max_node_idx != index:
        arr[max_node_idx], arr[index] = arr[index], arr[max_node_idx]
        down_heapify(arr, n, max_node_idx)
        
def build_heap(arr):
    """
    Converts array, arr to a max-heap by calling down_heapify() starting from last array index, and going upto 0
    """
    for i in range(len(arr)-1, -1, -1):
        down_heapify(arr, len(arr), i)
        
def heapsort(arr):
    """
    Performs heapsort on array, arr. Steps:
    1. convert the array to max-heap
    2. swap last element with first element (max element)
    3. call down_heapify() on first element, considering only n-1 entries of the array
    4. repeat steps, 2 and 3
    """
    
    # build max heap
    build_heap(arr)
    
    last_index = len(arr) - 1

    while last_index > 0:
        arr[last_index], arr[0] = arr[0], arr[last_index] # swap last element with max element
        down_heapify(arr, last_index, 0)
        last_index -= 1

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        raise ValueError("input list is empty!")

    heapsort(input_list)
    
    num_1, num_2 = 0, 0
    
    multiplier = 1
    idx = 0
    while idx < len(input_list)-1:
        num_1 += input_list[idx]*multiplier
        num_2 += input_list[idx+1]*multiplier
        multiplier *= 10
        idx += 2
    
    if idx < len(input_list):
        num_1 += input_list[idx]*multiplier
        
    return [num_1, num_2]

def test_rearrange_digits():
    print("\nTest case 1: ")
    list_1 = [1, 2, 3, 4, 5]
    print(f"\nInput List: {list_1}\n")
    print(rearrange_digits(list_1))
    # [531, 42]

    print("\nTest case 2: ")
    list_2 = [4, 6, 2, 5, 9, 8]
    print(f"\nInput List: {list_2}\n")
    print(rearrange_digits(list_2))
    # [852, 964]

    print("\nTest case 3: all zero list")
    list_3 = [0, 0, 0, 0]
    print(f"\nInput List: {list_3}\n")
    print(rearrange_digits(list_3))
    # [0, 0]

    print("\nTest case 4: empty list, to check input handling")
    list_4 = []
    print(f"\nInput List: {list_4}\n")
    print(rearrange_digits(list_4))
    # Traceback (most recent call last):
    #   File "problem_3.py", line 108, in <module>
    #     test_rearrange_digits()
    #   File "problem_3.py", line 99, in test_rearrange_digits
    #     print(rearrange_digits(list_4))
    #   File "problem_3.py", line 58, in rearrange_digits
    #     raise ValueError("input list is empty!")
    # ValueError: input list is empty!

if __name__ == "__main__":
    test_rearrange_digits()