# 6.0002 Problem Set 5
# Graph optimization
# Name:
# Collaborators:
# Time:

#
# Finding shortest paths through MIT buildings
#
import unittest
from graph_final import Digraph, Node, WeightedEdge

#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# Answer:
#


# Problem 2b: Implementing load_map
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
    file = open(map_filename, "r")
    graph = Digraph()

    for line in file:
        line = line.rstrip()
        src, dest, total_dist, total_dist_outdoors = line.split(" ")

        src = Node(src)
        dest = Node(dest)

        edge = WeightedEdge(src, dest, total_dist, total_dist_outdoors)

        if not graph.has_node(src):
            graph.add_node(src)
        if not graph.has_node(dest):
            graph.add_node(dest)

        graph.add_edge(edge)

    file.close()
    return graph

# Problem 3b: Implement get_best_path

def get_distance(digraph, path):
    total_dist = 0
    total_dist_outdoors = 0

    for i in range(len(path) - 1):
        for edge in digraph.get_edges_for_node(path[i]):
            # get all paths from node
            if edge.dest == path[i + 1]:
                # if there is a path with dest in graph
                total_dist += edge.get_total_distance()
                total_dist_outdoors += edge.get_outdoor_distance()

    return (total_dist, total_dist_outdoors)

def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist, best_path):
    """
    path: current path of nodes being traversed, total dist, total outdoor dist as int

    max_dist_outdoors: constraint

    best_dist: dist of best_path
    Return best_path: list of strings(nodes names), from src to dest
    """

    # path: empty list, append start
    path += [start]
    if start not in digraph.nodes: 
        raise ValueError("Node not in graph")
    elif start == end:
        return path
    else:
        # start in graph,
        # end not yet reached
        # seek for edges from start
        for edge in digraph.get_edges_for_node(start):
            # avoid to visit node already passed
            if edge.dest not in path:
                new_path = get_best_path(digraph, edge.dest, end, max_dist_outdoors, best_dist, best_path)
                if new_path != None:
                    # no path to dest
                    total_dist, outdoor_dist = getDistance(digraph, new_path)

                    if outdoor_dist <= max_dist_outdoors and total_dist <= best_dist:
                        best_path = new_path
                        best_dist = total_dist
                    # else: 
                        # None
    return best_path

# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    start = Node(start)
    end = Node(end)
    best_path = get_best_path(digraph, start, end, [], max_total_dist, max_dist_outdoors)

    if best_path == Node:
        raise ValueError("No such path")

    # best_path: list of node name
    return [node.get_name for node in best_path]

# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)


#if __name__ == "__main__":
#    unittest.main()
