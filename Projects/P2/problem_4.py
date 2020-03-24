def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in-place in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    
    left_index = 0
    right_index = len(input_list) - 1
    mid_index = 0
    
    while mid_index <= right_index:
        if input_list[mid_index] == 0:
            input_list[left_index], input_list[mid_index] = input_list[mid_index], input_list[left_index]
            left_index += 1
            mid_index += 1
        elif input_list[mid_index] == 2:
            input_list[right_index], input_list[mid_index] = input_list[mid_index], input_list[right_index]
            right_index -= 1
        else:
            mid_index += 1

def test_sort_012():

    print("\nTest case 1: input is an array of 0s, 1s, 2s")
    list_1 = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
    print(f"\nInput array: {list_1}")
    sort_012(list_1)
    print(f"\nSorted array: {list_1}")
    # Sorted array: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

    print("\nTest case 2: input is a sorted array of 0s, 1s, 2s")
    list_2 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
    print(f"\nInput array: {list_2}")
    sort_012(list_2)
    print(f"\nSorted array: {list_2}")
    # Sorted array: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

    print("\nTest case 3: input is an array of 0s, 1s")
    list_3 = [1, 0, 1, 1, 0, 0, 1, 1, 0]
    print(f"\nInput array: {list_3}")
    sort_012(list_3)
    print(f"\nSorted array: {list_3}")
    # Sorted array: [0, 0, 0, 0, 1, 1, 1, 1, 1]

    print("\nTest case 4: input is an array of 1s, 2s")
    list_4 = [1, 2, 1, 1, 2, 2, 1, 1, 2]
    print(f"\nInput array: {list_4}")
    sort_012(list_4)
    print(f"\nSorted array: {list_4}")
    # Sorted array: [1, 1, 1, 1, 1, 2, 2, 2, 2]

    print("\nTest case 5: input is an array of 0s, 2s")
    list_5 = [0, 2, 0, 0, 2, 2, 0, 2, 0]
    print(f"\nInput array: {list_5}")
    sort_012(list_5)
    print(f"\nSorted array: {list_5}")
    # Sorted array: [0, 0, 0, 0, 0, 2, 2, 2, 2]

    print("\nTest case 6: input is an empty array")  
    list_6 = []
    print(f"\nInput array: {list_6}")
    sort_012(list_6)
    print(f"\nSorted array: {list_6}")
    # Sorted array: []

if __name__ == "__main__":
    test_sort_012()
    