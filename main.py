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

def rev_string(s):
    # Reverses the input string using slicing
    return s[::-1]

# Test the function
print(rev_string("hello"))  # Output: "olleh"

def numwithin(x, start, end):
    # Checks if a number x falls within the range [start, end] (inclusive)
    return start <= x <= end

    # Test the function
    print(numwithin(3, 2, 4))  # Output: True
    print(numwithin(3, 1, 3))  # Output: True
    print(numwithin(10, 2, 5))  # Output: False