import random

#make a dictionary with keys as nodes and values as a list of nodes the key is connected to in the undirected graph 
row_dict = {}
with open("kargerMinCut.txt", "r") as file:
    for line in file:
        # Split the row into elements (assumes space or comma-separated values)
        elements = line.strip().split()
        
        # Convert to numbers (skipping the first element)
        row_dict[int(elements[0])] = [int(x) for x in elements[1:]]

#initialize nodes_left
nodes_left = []
for i in range(200):
    nodes_left.append(i + 1)

#choose random 2 nodes to fuse, deleting self loops
while len(nodes_left) > 2:
    #choose 2 random rows
    node_chosen_1 = random.choice(nodes_left)
    nodes_left.remove(node_chosen_1)
    node_chosen_2 = random.choice([n for n in row_dict[node_chosen_1] if n in nodes_left])
   
    #append contents of one row to another, deleting one row, removing self loops
    for i in row_dict[node_chosen_1]:
        if i not in row_dict[node_chosen_2] and i != node_chosen_2 and i != node_chosen_1:
            row_dict[node_chosen_2].append(i)

    if node_chosen_1 in row_dict[node_chosen_2]:
        row_dict[node_chosen_2].remove(node_chosen_1)

    del row_dict[node_chosen_1]

    #change element of all other lists from the deleted node to the new node number
    for i in nodes_left:
        if i != node_chosen_1:  # Avoid modifying the removed node
            row_dict[i] = [node_chosen_2 if x == node_chosen_1 else x for x in row_dict[i]]

final_cuts = 0
for key in row_dict.keys():
    final_cuts += (len(row_dict[key]))
final_cuts = 0.5 * final_cuts

if final_cuts < 20:
    print(int(final_cuts))