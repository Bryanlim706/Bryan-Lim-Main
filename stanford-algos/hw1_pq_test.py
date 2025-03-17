arr = []
try:
    with open("IntegerArray.txt", "r") as file:
        arr = [int(line.strip()) for line in file if line.strip()]
except FileNotFoundError:
    print("File not found.")

def count_inversions(arr):
    # Helper function for merge sort
    def merge_and_count(left, right):
        i = j = 0
        inversions = 0
        sorted_array = []
        
        # Merge the two halves and count inversions
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                inversions += len(left) - i  # All remaining elements in left are greater
                j += 1
        
        # Append remaining elements
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
        return sorted_array, inversions

    # Recursive function for merge sort and inversion counting
    def sort_and_count(array):
        if len(array) <= 1:
            return array, 0
        mid = len(array) // 2
        left, left_inversions = sort_and_count(array[:mid])
        right, right_inversions = sort_and_count(array[mid:])
        merged, split_inversions = merge_and_count(left, right)
        return merged, left_inversions + right_inversions + split_inversions

    _, total_inversions = sort_and_count(arr)
    return total_inversions
    
print(count_inversions(arr))