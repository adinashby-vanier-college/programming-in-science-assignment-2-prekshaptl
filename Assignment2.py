# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):

    max1 = max(numbers)

    rest = []
    for value in numbers:
        if value != max1:
            rest.append(value)

    if rest:
        max2 = max(rest)
    else:
        max2 = None

    return (max1, max2)

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):

    nonduplicatedlist = []
    for value in numbers:
        if value not in nonduplicatedlist:
            nonduplicatedlist.append(value)
    nonduplicatedlist.sort()
    return nonduplicatedlist

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    final_list = []
    running_total = 0

    for value in arr:
        running_total += value
        final_list.append(running_total)

    return final_list


# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    
    new = []

    for i in range(len(matrix[0])):
        new_row = []

        for j in range(len(matrix)):
            new_row.append(matrix[j][i])

        new.append(new_row)

    return new


# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    newlist = lst[0 : len(lst) : step]
 
    return newlist

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    tot = 0

    for i in range(len(list1)):
        tot = tot + (list1[i] * list2[i])

    return tot
    


# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):

    rows1 = len(matrix1)
    columns1 = len(matrix1[0])
    rows2 = len(matrix2)
    columns2 = len(matrix2[0])

    result = []

    for i in range(rows1):
        new_row = []

        for j in range(columns2):
            total = 0

            for k in range(columns1):
                total = total + (matrix1[i][k] * matrix2[k][j])

            new_row.append(total)

        result.append(new_row)

    return result
