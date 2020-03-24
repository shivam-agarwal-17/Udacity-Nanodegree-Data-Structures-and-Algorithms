def _sqrt_helper(number, lower, upper):
    if lower == upper:
        if number < upper*upper:
            return upper - 1
        else:
            return upper
        
    mid = (lower + upper)//2
    mid_sqr = mid * mid
    
    if mid_sqr == number:
        return mid
    elif mid_sqr < number:
        return _sqrt_helper(number, mid+1, upper)
    else:
        return _sqrt_helper(number, lower, mid-1)

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number < 0:
        raise ValueError('negative integers not supported!')

    if number == 0: # edge case 1
        return 0
    
    if number == 1: # edge case 2
        return 1
    
    return _sqrt_helper(number, 1, number-1)

def test_sqrt():
    print("\nTest case 1: floored square root of 9:")
    print(sqrt(9))
    # 3

    print("\nTest case 2: floored square root of 27:")
    print(sqrt(27))
    # 5

    print("\nTest case 3: floored square root of 0:")
    print(sqrt(0))
    # 0

    print("\nTest case 4: floored square root of 1:")
    print(sqrt(1))
    # 1

    print(f"\nTest case 5: floored square root of -1, to check input handling:")
    print(sqrt(-1))
    # Traceback (most recent call last):
    #   File "problem_1.py", line 56, in <module>
    #     print(sqrt(-1))
    #   File "problem_1.py", line 29, in sqrt
    #     raise ValueError('negative integers not supported!')
    # ValueError: negative integers not supported!

if __name__ == "__main__":
    test_sqrt()