import numpy as np

# 1. Create a 1D NumPy array of 10 integers and display the array, size, data type and dimensions.
print("\nPROGRAM 1")
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Array:", arr)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Dimensions:", arr.ndim)


# 2. Create two NumPy arrays of 5 integers and perform addition, subtraction, multiplication, division and modulus.
print("\nPROGRAM 2")
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([2, 4, 5, 8, 10])
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)
print("Modulus:", arr1 % arr2)


# 3. Create an array of 10 numbers and find maximum, minimum, sum and average.
print("\nPROGRAM 3")
arr = np.array([10, 25, 15, 40, 35, 50, 20, 45, 30, 5])
print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))


# 4. Create an array from 1 to 20 and display even and odd numbers using Boolean indexing.
print("\nPROGRAM 4")
arr = np.arange(1, 21)
even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]
print("Even Numbers:", even)
print("Odd Numbers:", odd)


# 5. Create a 1D array from 1 to 12 and reshape it into 2x6, 3x4 and 4x3 matrices.
print("\nPROGRAM 5")
arr = np.arange(1, 13)
print("2 x 6 Matrix:")
print(arr.reshape(2, 6))
print("3 x 4 Matrix:")
print(arr.reshape(3, 4))
print("4 x 3 Matrix:")
print(arr.reshape(4, 3))


# 6. Create two 3x3 matrices and perform matrix addition.
print("\nPROGRAM 6")
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

arr2 = np.array([[9, 8, 7],
                 [6, 5, 4],
                 [3, 2, 1]])

print("Matrix Addition:")
print(arr1 + arr2)


# 7. Create two compatible matrices and perform matrix multiplication using NumPy.
print("\nPROGRAM 7")
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[1, 2],
                 [3, 4],
                 [5, 6]])

print("Matrix Multiplication:")
print(np.matmul(arr1, arr2))


# 8. Create a 3x4 matrix and find its transpose.
print("\nPROGRAM 8")
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("Original Matrix:")
print(arr)
print("Transpose:")
print(arr.T)


# 9. Create a 4x4 matrix and display the first row, last column, diagonal and second and third rows.
print("\nPROGRAM 9")
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("First Row:", arr[0])
print("Last Column:", arr[:, -1])
print("Diagonal:", np.diag(arr))
print("Second and Third Rows:")
print(arr[1:3])


# 10. Create a 4x4 matrix and find the sum of each row and each column.
print("\nPROGRAM 10")
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Row Sum:", np.sum(arr, axis=1))
print("Column Sum:", np.sum(arr, axis=0))


# 11. Create an array from 1 to 20 and display the first 5, last 5, alternate elements and reverse order.
print("\nPROGRAM 11")
arr = np.arange(1, 21)
print("First 5:", arr[:5])
print("Last 5:", arr[-5:])
print("Alternate Elements:", arr[::2])
print("Reverse:", arr[::-1])


# 12. Create an array of 10 integers and replace all elements greater than 50 with 0.
print("\nPROGRAM 12")
arr = np.array([20, 65, 40, 75, 30, 90, 55, 10, 80, 45])
arr[arr > 50] = 0
print("Array:", arr)


# 13. Create an unsorted array and display it in ascending and descending order.
print("\nPROGRAM 13")
arr = np.array([45, 12, 78, 23, 9, 56, 34])
print("Original Array:", arr)
print("Ascending:", np.sort(arr))
print("Descending:", np.sort(arr)[::-1])


# 14. Create an array containing duplicate elements and display only unique elements.
print("\nPROGRAM 14")
arr = np.array([10, 20, 10, 30, 20, 40, 30, 50, 10])
print("Array:", arr)
print("Unique Elements:", np.unique(arr))


# 15. Create two arrays and perform horizontal and vertical concatenation.
print("\nPROGRAM 15")
arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6],
                 [7, 8]])

print("Horizontal Concatenation:")
print(np.hstack((arr1, arr2)))

print("Vertical Concatenation:")
print(np.vstack((arr1, arr2)))


# 16. Create an array of marks of 10 students and find highest, lowest, average, median and standard deviation.
print("\nPROGRAM 16")
marks = np.array([75, 82, 68, 90, 85, 72, 95, 60, 88, 78])

print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))


# 17. Create marks of 20 students, find the class average and display marks above the average.
print("\nPROGRAM 17")
marks = np.array([65, 78, 85, 90, 55, 72, 88, 95, 60, 70,
                  82, 75, 68, 91, 58, 80, 73, 87, 66, 79])

average = np.mean(marks)

print("Class Average:", average)
print("Above Average Marks:", marks[marks > average])


# 18. Create a 3D array of shape (2,3,4) containing values from 1 to 24 and display array, dimensions, shape and size.
print("\nPROGRAM 18")
arr = np.arange(1, 25).reshape(2, 3, 4)

print("Array:")
print(arr)
print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)


# 19. Create a 3D array of shape (2,3,4) and access the first, last, [0,1,2] and [1,2,3] elements.
print("\nPROGRAM 19")
arr = np.arange(1, 25).reshape(2, 3, 4)

print("First Element:", arr[0, 0, 0])
print("Last Element:", arr[1, 2, 3])
print("Element at [0,1,2]:", arr[0, 1, 2])
print("Element at [1,2,3]:", arr[1, 2, 3])







# 20. Create a 3D array of shape (2,3,4) and find the sum of all elements, each layer, rows and columns.
print("\nPROGRAM 20")
arr = np.arange(1, 25).reshape(2, 3, 4)

print("Sum of All Elements:", np.sum(arr))
print("Sum of Each Layer:", np.sum(arr, axis=(1, 2)))
print("Sum Along Rows:", np.sum(arr, axis=1))
print("Sum Along Columns:", np.sum(arr, axis=2))


# 21. Create a random 3D array and replace all values greater than 50 with 0.
print("\nPROGRAM 21")
arr = np.random.randint(1, 101, (2, 3, 4))

print("Original Array:")
print(arr)

arr[arr > 50] = 0

print("Updated Array:")
print(arr)


# 22. Create a random 3D array of shape (3,4,5) and find mean, median, standard deviation, variance, minimum and maximum.
print("\nPROGRAM 22")
arr = np.random.randint(1, 101, (3, 4, 5))

print("Array:")
print(arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))


# 23. Create a 3D array of shape (2,3,4), flatten it and display the original and flattened array.
print("\nPROGRAM 23")
arr = np.arange(1, 25).reshape(2, 3, 4)

print("Original Array:")
print(arr)

flat = arr.flatten()

print("Flattened Array:")
print(flat)


# 24. Create a 3D array of integers from 1 to 27, flatten it and find sum, average, maximum and minimum.
print("\nPROGRAM 24")
arr = np.arange(1, 28).reshape(3, 3, 3)

flat = arr.flatten()

print("Original Array:")
print(arr)

print("Flattened Array:", flat)
print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))


# 25. Create a random 3D array of shape (3,4,5), flatten it and display values greater than 50, even values and values less than average.
print("\nPROGRAM 25")
arr = np.random.randint(1, 101, (3, 4, 5))

flat = arr.flatten()
average = np.mean(flat)

print("Array:")
print(arr)

print("Greater Than 50:")
print(flat[flat > 50])

print("Even Numbers:")
print(flat[flat % 2 == 0])

print("Less Than Average:")
print(flat[flat < average])
