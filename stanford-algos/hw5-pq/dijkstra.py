import heapq

#load data into array node, node number 1st
data_list = []
with open('dijkstra-data.txt', 'r') as file:
    for line in file:
        line = line.strip()
        values = line.split('\t')
        key = int(values[0])
        formatted_values = [(int(val.split(',')[0]),int(val.split(',')[1])) for val in values[1:]]
        data_list.append({key:formatted_values})

#initialize array, node number 1st
infinity = float('inf')
answers = [(i + 1, infinity) for i in range(200)]
answers[0] = (1, 0)

#initialize min heap, weight 1st
min_heap = [(0,1)]

#main
while min_heap:
    min_node = heapq.heappop(min_heap)

    row = data_list[int(min_node[1]) - 1]
    for pair in row[int(min_node[1])]:
        new_dist = answers[int(min_node[1]) - 1][1] + int(pair[1])
        if new_dist < answers[int(pair[0]) - 1][1]:
            answers[int(pair[0]) - 1] = (int(pair[0]), int(new_dist))
            heapq.heappush(min_heap,(new_dist, int(pair[0])))
        
        
print(answers)
