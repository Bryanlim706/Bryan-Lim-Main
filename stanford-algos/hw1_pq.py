#count number of inversions for a bunch of numbers
numbers = []
try:
    with open("IntegerArray.txt", "r") as file:
        numbers = [int(line.strip()) for line in file if line.strip()]
except FileNotFoundError:
    print("File not found.")

#function that divides large array in 2, count inversions within each subarray(by calling the function), and count split inversions while rejoining subarrays,
#returning final sorted array and number of inversions

#function
def count_inversions(array):
    #if n more than 1
    if len(array) > 1:
        #divide large array in 2
        middle = len(array) // 2
        #call function on each half, returning full sorted array and amt of localised inversions
        left_array, left_count = count_inversions(array[:middle])
        right_array, right_count = count_inversions(array[middle:])
        #count number of split inversions between both subarrays while re-sorting
        sorted_array=[]
        split_counter = 0
        i, j = 0, 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                sorted_array.append(left_array[i])
                i += 1
            else:
                sorted_array.append(right_array[j])
                split_counter += len(left_array) - i
                j += 1
        sorted_array.extend(left_array[i:])
        sorted_array.extend(right_array[j:])

        return sorted_array, split_counter + left_count + right_count
        #return full sorted array and total number of inversions (left+right+split cfdx5r5)
    #if n is 1
    if len(array) <= 1:
        return array, 0
        #return array and total number of inversions = 0

#run function
_, inversions = count_inversions(numbers)
print(inversions)

