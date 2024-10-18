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

    def pascal(n):
    # Generates and prints the first n rows of Pascal's triangle
    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        row = [1]  # Each row starts with 1
        # Compute the values for the middle of the row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Each row ends with 1
        triangle.append(row)  # Add the completed row to the triangle

    # Print each row of Pascal's triangle
    for row in triangle:
        print(row)

# Test the function
pascal(5)
# Output:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]