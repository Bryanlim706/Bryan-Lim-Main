number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    first_line = input().split()
    starting_tower_index = int(first_line[1])

    number_of_towers = int(first_line[0])
    height_of_towers = input().split
    starting_tower_height = int(height_of_towers[starting_tower_index - 1])
    arr = height_of_towers.sort()
    threshold = starting_tower_height
    arr = [x for x in arr if x >= threshold]
    arr.insert(0,starting_tower_height)

