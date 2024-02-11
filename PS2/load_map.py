import unittest
from graph_final import Digraph, Node, WeightedEdge
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """

    data_file = open(map_filename, "r")
    map_graph = Digraph()

    for line in data_file:
        line = line.rstrip()
        src_node, dest_node, total_distance, outdoor_distance = line.split(" ")

        # Register src dest as Node
        src = Node(src_node)
        dest = Node(dest_node)

        # Register Edge with given data
        edge = WeightedEdge(src, dest, total_distance, outdoor_distance)

        # Register all data to map_graph
        if not map_graph.has_node(src):
            map_graph.add_node(src)

        if not map_graph.has_node(dest):
            map_graph.add_node(dest)

        map_graph.add_edge(edge)

    print("Loading map from file...")
    return map_graph

graph = load_map("mit_map.txt")
print(graph)

print(graph.has_node(Node("32")))
