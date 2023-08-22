def sqrt(x):
    # Base cases
    if x == 0 or x == 1:
        return x

    # Binary search for the square root
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Test cases
print(sqrt(4))  
print(sqrt(9)) 
print(sqrt(16))
