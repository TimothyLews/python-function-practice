def max_num(a, b, c):
    # Returns the maximum of three numbers
    return max(a, b, c)

# Test the function
print(max_num(1, 5, 3))  # Output: 5

def mult_list(lst):
    # Multiplies all elements in a list together
    result = 1
    for num in lst:
        result *= num  # Multiply each number with the current result
    return result

# Test the function
print(mult_list([2, 3, 4]))  # Output: 24
