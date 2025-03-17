import random

cuts = 100000
for i in range(1000):
    #make a dictionary with keys as nodes and values as a list of nodes the key is connected to in the undirected graph 
    row_dict = {}
    with open("kargerMinCut.txt", "r") as file:
        for row_number, line in enumerate(file, start=1):
            # Split the row into elements (assumes space or comma-separated values)
            elements = line.strip().split()
        
            # Convert to numbers (skipping the first element)
            row_dict[row_number] = [float(x) for x in elements[1:]]

    with open("kargerMinCut.txt", "r") as file:
        row_count = sum(1 for _ in file)

    #initialize nodes_left
    nodes_left = []
    for i in range(200):
        nodes_left.append(i + 1)

    #choose random 2 nodes to fuse, deleting self loops
    while len(nodes_left) > 2:
        #choose 2 random rows
        node_chosen_1 = random.choice(nodes_left)
        nodes_left.remove(node_chosen_1)
        node_chosen_2 = random.choice(nodes_left)
   
    #append contents of one row to another, deleting one row, removing self loops
    for i in row_dict[node_chosen_1]:
        row_dict[node_chosen_2].append(i)


    del row_dict[node_chosen_1]


    for i in row_dict[node_chosen_2]:
        if i == node_chosen_1 or i == node_chosen_2:
            row_dict[node_chosen_2].remove(i)

    final_cuts = 0
    for key in row_dict.keys():
        final_cuts += (len(row_dict[key]))
        final_cuts = 0.5 * final_cuts

    if final_cuts < cuts:
        cuts = final_cuts

print(cuts)