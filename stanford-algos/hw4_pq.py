#kosaraju's algorithm

#datastruct node = int node number, int array of outgoing arc numbers, boolean, int finishing time, 
class node:
    def __init___(self, node_number, outgoing_arcs_destinations, explored_status, finishing_time):
        self.node_number = node_number
        self.outgoing_arcs_destinations = outgoing_arcs_destinations
        self.explored_status = explored_status
        self.finishing_time = finishing_time

#function DFS-loop: input = graph




#load file into dictionaries in reverse order(name of node: array of name of nodes outgoing edges reach in reverse graph)
def load_graph(filename):
    with open()

#randomise all node[finishing time]
#initialize all node[boolean] == false for unexplored
#DFS-loop (assign all nodes with magical finishing time)

#empty all node[array of outgoing arc numbers] and node[node number] then load file into dictionaries in normal order
#initialize all node[boolean] == false for unexplored
#DFS-loop (for SCC[i] being the global variable that i increments every new leader node, SCC[i] += 1 every DFS called, to count size of SCCs)
