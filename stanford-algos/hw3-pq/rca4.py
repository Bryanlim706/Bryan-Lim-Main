import random

# Make a dictionary with keys as nodes and values as a list of nodes the key is connected to in the undirected graph
row_dict = {}
with open("kargerMinCut.txt", "r") as file:
    for line in file:
        # Split the row into elements (assumes space or comma-separated values)
        elements = line.strip().split()
        
        # Convert to numbers (skipping the first element)
        row_dict[int(elements[0])] = [int(x) for x in elements[1:]]

# Initialize nodes_left
nodes_left = []
for i in range(200):
    nodes_left.append(i + 1)

# Choose random 2 nodes to fuse, deleting self loops
while len(nodes_left) > 2:
    # Choose 2 random nodes
    node_chosen_1 = random.choice(nodes_left)
    nodes_left.remove(node_chosen_1)

    # Find a node connected to node_chosen_1 that's still in nodes_left
    node_chosen_2 = random.choice([n for n in row_dict[node_chosen_1] if n in nodes_left])

    # Append contents of one row to another, deleting one row, removing self loops
    for i in row_dict[node_chosen_1]:
        if i != node_chosen_2 and i != node_chosen_1 and i not in row_dict[node_chosen_2]:
            row_dict[node_chosen_2].append(i)

    # Remove self-loop if it exists
    if node_chosen_1 in row_dict[node_chosen_2]:
        row_dict[node_chosen_2].remove(node_chosen_1)

    # Delete the row for the fused node
    del row_dict[node_chosen_1]

    # Change elements of all other lists from the deleted node to the new node number
    for i in nodes_left:
        if i != node_chosen_1:  # Avoid modifying the removed node
            row_dict[i] = [node_chosen_2 if x == node_chosen_1 else x for x in row_dict[i]]

    # Add the new fused node back to the list of nodes left
    nodes_left.append(node_chosen_2)

# Calculate the number of cuts (edges) in the final graph
final_cuts = sum(len(row_dict[key]) for key in row_dict.keys()) // 2

if final_cuts < 20:
    print(int(final_cuts))