#populate numbers array
data_array = []
with open("median.txt", "r") as file:
    for number in file:
        number = int(number.strip())
        data_array.append(number)

#initialize both heaps, add first two numbers
min_heap = []
max_heap = []
first_number = data_array.pop(0)
second_number = data_array.pop(0)
if first_number > second_number:
    min_heap.append(first_number)
    max_heap.append(second_number)
else:
    min_heap.append(second_number)
    max_heap.append(first_number)

print(max_heap)
print(min_heap)

#insert & heapify max heap function
def insert_heapify_max(number):
    max_heap.append(number)

    child_index = len(max_heap) - 1
    while child_index > 0       :
        parent_index = (child_index - 1) // 2
        if max_heap[child_index] > max_heap[parent_index]:
            max_heap[child_index], max_heap[parent_index] = max_heap[parent_index], max_heap[child_index]
            child_index = parent_index
        else:
            break

#insert & heapify min heap function
def insert_heapify_min(number):
    min_heap.append(number)

    child_index = len(min_heap) - 1
    while child_index > 0       :
        parent_index = (child_index - 1) // 2
        if min_heap[child_index] < min_heap[parent_index]:
            min_heap[child_index], min_heap[parent_index] = min_heap[parent_index], min_heap[child_index]
            child_index = parent_index
        else:
            break

#balance heaps function
def balance_heaps():
    if len(min_heap) > len(max_heap) + 1:
        xx
    elif len(max_heap) > len(min_heap) + 1:
        max_heap[0], max_heap[-1] = max_heap[-1], max_heap[0]
        largest_number = max_heap.pop()
        insert_heapify_min(largest_number)

        #heapify max_heap
        parent_index = 0
        while len(max_heap) >= ((parent_index * 2) + 1) + 1: #while not if no children nodes
            left_index = (parent_index * 2) + 1
            right_index = (parent_index * 2) + 2
            left_child = max_heap[left_index]
            if right_index < len(max_heap):
                right_child = max_heap[right_index]
            if len(max_heap) == right_index: #if one child node
                if left_child > max_heap[parent_index]:
                    max_heap[left_index], max_heap[parent_index] = max_heap[parent_index], max_heap[left_index]
                    break
            else: #if two child nodes
                if max_heap[parent_index] >= left_child and max_heap[parent_index] >= right_child:
                    break
                else:
                    if max_heap[parent_index] < left_child and max_heap[parent_index] > right_child:
                        max_heap[left_index], max_heap[parent_index] = max_heap[parent_index], max_heap[left_index]
                        parent_index = left_index #change parent
                    elif max_heap[parent_index] > left_child and max_heap[parent_index] < right_child:
                        max_heap[right_index], max_heap[parent_index] = max_heap[parent_index], max_heap[right_index]
                        parent_index = right_index #change parent
                    else:
                        if left_child > right_child:
                            max_heap[left_index], max_heap[parent_index] = max_heap[parent_index], max_heap[left_index]
                            parent_index = left_index #change parent
                        else:
                            max_heap[right_index], max_heap[parent_index] = max_heap[parent_index], max_heap[right_index]
                            parent_index = right_index #change parent

    

#main
while True:
    if len(data_array) == 0:
        break
    number = data_array.pop(0)
    if number > max_heap[0] and number < min_heap[0]:
        if len(min_heap) > len(max_heap):
            insert_heapify_max(number)
        else:
            insert_heapify_min(number)

    elif number <= max_heap[0]:
        insert_heapify_max(number)
        balance_heaps()
    else:
        insert_heapify_min(number)
        balance_heaps()

        




