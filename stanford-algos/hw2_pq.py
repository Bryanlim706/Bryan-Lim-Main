#Quicksort algorithm with first element as pivot, counting nuber of comparisons
numbers = []
try:
    with open("QuickSort.txt", "r") as file:
        numbers = [int(line.strip()) for line in file if line.strip()]
except FileNotFoundError:
    print("File not found.")


def quicksort(array):
    # Function that partitions the array and counts comparisons
    def pivot_subroutine(array):
        if len(array) <= 1:  # Base case: single-element or empty array
            return array, 0
        
        # Use the first element as the pivot
        pivot = array[0]
        i = 1  # Pointer for the boundary of the "less than pivot" subarray
        compare_counter = len(array) - 1  # Number of comparisons in this partition
        
        # Partitioning step
        for j in range(1, len(array)):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]  # Swap elements
                i += 1
        
        # Place the pivot in its correct position
        array[0], array[i - 1] = array[i - 1], array[0]
        
        # Recursively sort the left and right subarrays
        left, left_counter = quicksort(array[:i - 1])
        right, right_counter = quicksort(array[i:])
        
        # Combine results
        new_array = left + [pivot] + right
        total_comparisons = compare_counter + left_counter + right_counter
        return new_array, total_comparisons

    # Call the subroutine and return its result
    return pivot_subroutine(array)

_, total_comparisons = quicksort(numbers)
print(total_comparisons)
