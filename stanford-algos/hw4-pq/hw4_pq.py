#kosaraju's algorithm
import sys

sys.setrecursionlimit(10**5)

#globals
normal_graph, reverse_graph = [], []
finishing_time_heap_of_row_numbers = []
SCC_size_counter = [0] * 875715


def load_graph(filename):
    with open(filename, "r") as textfile:
        for i in range(1, 875714 + 1):
            normal_graph.append({"node_number": i, "outgoing_arcs": [], "explored_status": False})
            reverse_graph.append({"node_number": i, "outgoing_arcs": [], "explored_status": False,})
        for row in textfile:
            first_number, second_number = map(int, row.split())
            normal_graph[first_number - 1]["outgoing_arcs"].append(second_number)
            reverse_graph[second_number - 1]["outgoing_arcs"].append(first_number)

#first round
def dfs_on_graph(graph):
    for row_number in range(875714):
        if graph[row_number]["explored_status"] == False:
            dfs_on_node(graph, row_number)

def dfs_on_node(graph, row_number):
    graph[row_number]["explored_status"] = True
    
    for neighbour in graph[row_number]["outgoing_arcs"]:
        neighbour_row_number = neighbour - 1
        if graph[neighbour_row_number]["explored_status"] == False:
            dfs_on_node(graph, neighbour_row_number)
    finishing_time_heap_of_row_numbers.append(row_number)

#second round
def dfs_on_graph_2(graph):
    for row_number in reversed(finishing_time_heap_of_row_numbers):
        if graph[row_number]["explored_status"] == False:
            leader_row = row_number
            dfs_on_node_2(graph, row_number, leader_row)

def dfs_on_node_2(graph, row_number, leader_row):
    graph[row_number]["explored_status"] = True

    global SCC_size_counter
    SCC_size_counter[leader_row] += 1
    
    for neighbour in graph[row_number]["outgoing_arcs"]:
        neighbour = neighbour - 1
        if graph[neighbour]["explored_status"] == False:
            dfs_on_node_2(graph, neighbour, leader_row)

def print_top5(array_of_SCC_sizes):
    array = sorted(array_of_SCC_sizes, reverse=True)
    for i in range(5):
        print(array[i])


load_graph("SCC.txt")
dfs_on_graph(reverse_graph)
dfs_on_graph_2(normal_graph)
print_top5(SCC_size_counter)

        
    

#randomise all node[finishing time]
#initialize all node[boolean] == false for unexplored
#DFS-loop (assign all nodes with magical finishing time)

#empty all node[array of outgoing arc numbers] and node[node number] then load file into dictionaries in normal order
#initialize all node[boolean] == false for unexplored
#DFS-loop (for SCC[i] being the global variable that i increments every new leader node, SCC[i] += 1 every DFS called, to count size of SCCs)
