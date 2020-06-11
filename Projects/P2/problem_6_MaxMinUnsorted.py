def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    
    if len(ints) == 0: # empty list
        return None
    
    _min, _max = ints[0], ints[0]
    
    for idx in range(1, len(ints)):
        num = ints[idx]
        if num < _min:
            _min = num
        if num > _max:
            _max = num
    
    return (_min, _max)

def test_get_min_max():
    
    print("\nTest case 1: input list contains both positive and negative integers")
    l1 = [5, 0, 1, 2, 3, 2, 9, 8, 10, -1]
    print(f"\nInput array: {l1}")
    print(f"\n(Min, Max): {get_min_max(l1)}")
    # (Min, Max): (-1, 10)

    print("\nTest case 2: input list contains repetition of single integer")
    l2 = [5, 5, 5, 5, 5, 5]
    print(f"\nInput array: {l2}")
    print(f"\n(Min, Max): {get_min_max(l2)}")
    # (Min, Max): (5, 5)

    print("\nTest case 3: input list is empty")
    l3 = []
    print(f"\nInput array: {l3}")
    print(f"\n(Min, Max): {get_min_max(l3)}")
    # (Min, Max): None

if __name__ == "__main__":
    test_get_min_max()
