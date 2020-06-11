def  _search_pivot_helper(arr, start, end):
    """Search for the pivot, returns -1, if no pivot found i.e. array is already sorted. Pivot defined as the element 
    at the boundary. For example, in case of arr = [4,5,6,7,0,1,2], pivot will be 3 (i.e. index for element 7)"""
    
    if end < start:
        return -1
    
    mid = (start + end) // 2
    
    if mid < end and arr[mid] > arr[mid+1]: # 'mid < end' check is to ensure that mid+1 index exists
        return mid
    
    if mid > start and arr[mid] < arr[mid-1]:
        return mid-1
        
    if arr[mid] < arr[end]: # part from mid to end is sorted, that means pivot sould be in part between start to mid-1
        return _search_pivot_helper(arr, start, mid-1)

    else: # pivot sould be in part between mid+1 to end
        return _search_pivot_helper(arr, mid+1, end)

def search_pivot(arr):
    return _search_pivot_helper(arr, 0, len(arr)-1)

def _rotated_array_search_helper(input_list, number, start_index, end_index):
    """
    Helper for rotated_array_search() method.

    Args:
       input_list(array): input array to search
       number(int): Target
       start_index: start index of the array + pivot
       end_index: end index of the array + pivot
    Returns: 
       int: Index or -1
    """
    
    if start_index > end_index:
        return -1
    
    mid = (start_index + end_index)//2
    mid_index = mid % len(input_list)
        
    if input_list[mid_index] == number:
        return mid_index
    elif input_list[mid_index] < number:
        return _rotated_array_search_helper(input_list, number, mid+1, end_index)
    else:
        return _rotated_array_search_helper(input_list, number, start_index, mid-1)

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    
    pivot = search_pivot(input_list)+1 # see definition of pivot under _search_pivot_helper() definition
    return _rotated_array_search_helper(input_list, number, pivot, len(input_list)-1+pivot)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_rotated_sorted_array_search(test_case_num, test_case, test_case_str):
    print(f"\nTest case {test_case_num}: {test_case_str}\n")

    input_list, number = test_case

    print(f"Input list: {input_list}\n")
    print(f"Number:  {number}\n")
    print(f"Output: {rotated_array_search(input_list, number)}\n")
    print(f"Expected Output: {linear_search(input_list, number)}\n")

if __name__ == "__main__":
    
    input_list = [1, 2, 3, 4, 6, 7, 8, 9, 10]

    # Search for input_list[0] in above input_list rotated by all possible shifts from 0 to len(input_list)-1
    test_case_num = 1
    rotate = lambda l, n : l[n:] + l[:n]
    for shift in range(len(input_list)):
        rot_list = rotate(input_list, shift)
        test_rotated_sorted_array_search(test_case_num, (rot_list, input_list[0]), f"Search in sorted input list rotated left by {shift}")
        test_case_num += 1

    # Search for element not present in input_list
    test_rotated_sorted_array_search(test_case_num, (input_list, 11), "Search for an element NOT present in the input list")






