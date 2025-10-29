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



        min_heap[0], min_heap[-1] = min_heap[-1], min_heap[0]
        largest_number = min_heap.pop()
        insert_heapify_max(largest_number)

        #heapify min_heap
        parent_index = 0
        while len(min_heap) >= ((parent_index * 2) + 1) + 1: #while not if no children nodes
            left_index = (parent_index * 2) + 1
            right_index = (parent_index * 2) + 2
            left_child = min_heap[left_index]
            if right_index < len(min_heap):
                right_child = min_heap[right_index]
            if len(min_heap) == right_index: #if one child node
                if left_child > min_heap[parent_index]:
                    min_heap[left_index], min_heap[parent_index] = min_heap[parent_index], min_heap[left_index]
                    break
            else: #if two child nodes
                if min_heap[parent_index] >= left_child and min_heap[parent_index] >= right_child:
                    break
                else:
                    if min_heap[parent_index] < left_child and min_heap[parent_index] > right_child:
                        min_heap[left_index], min_heap[parent_index] = min_heap[parent_index], min_heap[left_index]
                        parent_index = left_index #change parent
                    elif min_heap[parent_index] > left_child and min_heap[parent_index] < right_child:
                        min_heap[right_index], min_heap[parent_index] = min_heap[parent_index], min_heap[right_index]
                        parent_index = right_index #change parent
                    else:
                        if left_child > right_child:
                            min_heap[left_index], min_heap[parent_index] = min_heap[parent_index], min_heap[left_index]
                            parent_index = left_index #change parent
                        else:
                            min_heap[right_index], min_heap[parent_index] = min_heap[parent_index], min_heap[right_index]
                            parent_index = right_index #change parent