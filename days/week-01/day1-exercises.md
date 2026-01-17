# Day 1: Getting Started with Python and NumPy

## Exercises

### Exercise 1: Python Basics
```python
# TODO: Complete these basic Python exercises

# 1. Create a function that takes a list of numbers and returns the sum
def sum_numbers(numbers):
    # Your code here
    pass

# 2. Create a function that filters even numbers from a list
def filter_even(numbers):
    # Your code here
    pass

# 3. Create a function that reverses a string
def reverse_string(text):
    # Your code here
    pass

# Test your functions
print(sum_numbers([1, 2, 3, 4, 5]))  # Should print 15
print(filter_even([1, 2, 3, 4, 5, 6]))  # Should print [2, 4, 6]
print(reverse_string("hello"))  # Should print "olleh"
```

### Exercise 2: NumPy Arrays
```python
import numpy as np

# TODO: Complete these NumPy exercises

# 1. Create a 3x3 array filled with zeros
zeros_array = None  # Your code here

# 2. Create a 2x3 array filled with ones
ones_array = None  # Your code here

# 3. Create an array with values from 0 to 9
range_array = None  # Your code here

# 4. Create a 3x3 identity matrix
identity_matrix = None  # Your code here

# 5. Create a 4x4 array with random values
random_array = None  # Your code here

print("Zeros:", zeros_array)
print("Ones:", ones_array)
print("Range:", range_array)
print("Identity:", identity_matrix)
print("Random:", random_array)
```

### Exercise 3: Array Operations
```python
import numpy as np

# Given arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# TODO: Perform these operations

# 1. Add arrays a and b
result_add = None  # Your code here

# 2. Multiply arrays a and b element-wise
result_multiply = None  # Your code here

# 3. Calculate the dot product of a and b
dot_product = None  # Your code here

# 4. Find the mean of array a
mean_a = None  # Your code here

# 5. Find the maximum value in array b
max_b = None  # Your code here

print("Addition:", result_add)
print("Multiplication:", result_multiply)
print("Dot Product:", dot_product)
print("Mean of a:", mean_a)
print("Max of b:", max_b)
```

### Exercise 4: Matrix Operations
```python
import numpy as np

# Create matrices
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# TODO: Perform these operations

# 1. Matrix multiplication
matrix_product = None  # Your code here

# 2. Transpose of matrix_a
transpose_a = None  # Your code here

# 3. Determinant of matrix_a
det_a = None  # Your code here (hint: np.linalg.det)

# 4. Inverse of matrix_a
inverse_a = None  # Your code here (hint: np.linalg.inv)

print("Matrix Product:\n", matrix_product)
print("Transpose:\n", transpose_a)
print("Determinant:", det_a)
print("Inverse:\n", inverse_a)
```

### Exercise 5: Reshaping and Indexing
```python
import numpy as np

# Create an array
arr = np.arange(12)

# TODO: Complete these tasks

# 1. Reshape arr to 3x4
reshaped = None  # Your code here

# 2. Get the first row of reshaped
first_row = None  # Your code here

# 3. Get the last column of reshaped
last_column = None  # Your code here

# 4. Get elements greater than 5
greater_than_5 = None  # Your code here

print("Original:", arr)
print("Reshaped:\n", reshaped)
print("First Row:", first_row)
print("Last Column:", last_column)
print("Greater than 5:", greater_than_5)
```

### Bonus Challenge: Simple Linear Algebra
```python
import numpy as np

# TODO: Solve this system of equations using NumPy
# 2x + 3y = 13
# x - y = -1

# Hint: Create coefficient matrix A and constants vector b
# Then use np.linalg.solve(A, b)

A = None  # Your code here
b = None  # Your code here
solution = None  # Your code here

print("Solution: x =", solution[0], ", y =", solution[1])
# Expected: x = 2, y = 3
```

## Solutions
<details>
<summary>Click to see solutions (try solving first!)</summary>

### Exercise 1 Solutions
```python
def sum_numbers(numbers):
    return sum(numbers)

def filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]

def reverse_string(text):
    return text[::-1]
```

### Exercise 2 Solutions
```python
zeros_array = np.zeros((3, 3))
ones_array = np.ones((2, 3))
range_array = np.arange(10)
identity_matrix = np.eye(3)
random_array = np.random.rand(4, 4)
```

### Exercise 3 Solutions
```python
result_add = a + b
result_multiply = a * b
dot_product = np.dot(a, b)
mean_a = np.mean(a)
max_b = np.max(b)
```

### Exercise 4 Solutions
```python
matrix_product = np.matmul(matrix_a, matrix_b)
transpose_a = matrix_a.T
det_a = np.linalg.det(matrix_a)
inverse_a = np.linalg.inv(matrix_a)
```

### Exercise 5 Solutions
```python
reshaped = arr.reshape(3, 4)
first_row = reshaped[0, :]
last_column = reshaped[:, -1]
greater_than_5 = arr[arr > 5]
```

### Bonus Solution
```python
A = np.array([[2, 3], [1, -1]])
b = np.array([13, -1])
solution = np.linalg.solve(A, b)
```
</details>

## Next Steps
Once you complete these exercises:
1. Document what you learned in your daily log
2. Try creating your own exercises
3. Move on to Day 2 materials
4. Share your progress!

Good luck! 🚀
