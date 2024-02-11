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

def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors, toPrint=False):
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
    # convert string to node
    if digraph.has_node(Node(start)) and digraph.has_node(Node(end)):
        startNode = digraph.get_node(start)
        endNode = digraph.get_node(end)
    else:
        raise ValueError("Node not in graph")

    initPath = [startNode]
    pathQueue = [initPath]
    currentDistance = None
    selectedPaths, selectedDistance = [], []
    prevTotalDist = None

    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        lastNode = tmpPath[-1]

        if lastNode == endNode:
            total_dist, total_dist_outdoors = 0, 0
            breakForLoop = False

            # weight the edges of tmpPath
            for i in range(len(tmpPath) - 1):
                if not breakForLoop:

                    if prevTotalDist == None:
                        pathDistance = int(digraph.get_edge(tmpPath[i], tmpPath[i+1]).get_total_distance())
                        pathDistanceOutdoors = int(digraph.get_edge(tmpPath[i], tmpPath[i+1]).get_outdoor_distance())

                        if total_dist + pathDistance <= max_total_dist and total_dist_outdoors + pathDistanceOutdoors <= max_dist_outdoors:
                            total_dist += pathDistance
                            total_dist_outdoors += pathDistanceOutdoors

                        else:
                            breakForLoop = True

                    else:
                        pathDistance = int(digraph.get_edge(tmpPath[i], tmpPath[i+1]).get_total_distance())
                        pathDistanceOutdoors = int(digraph.get_edge(tmpPath[i], tmpPath[i+1]).get_outdoor_distance())

                        if total_dist + pathDistance <= prevTotalDist and total_dist_outdoors + pathDistanceOutdoors <= max_dist_outdoors:
                            total_dist += pathDistance
                            total_dist_outdoors += pathDistanceOutdoors

                        else:
                            breakForLoop = True
                else:
                    break

            if not breakForLoop:
                if currentDistance == None:
                    # initialize current distance and override by getting less values
                    currentDistance = (total_dist, total_dist_outdoors)
                    prevTotalDist = total_dist
                    selectedPaths.append(tmpPath)
                    selectedDistance.append(currentDistance)

                    if toPrint:
                        print("current selectedPaths:", selectedPaths)
                        print("current selectedDistance:", selectedDistance)

                else:
                    if total_dist == currentDistance[0]:
                        selectedPaths.append(tmpPath)
                        selectedDistance.append(currentDistance)
                        if toPrint:
                            print("current selectedPaths:", selectedPaths)
                            print("current selectedDistance:", selectedDistance)

                    elif total_dist < currentDistance[0]:
                        currentDistance = (total_dist, total_dist_outdoors)
                        prevTotalDist = total_dist
                        selectedPaths.append(tmpPath)
                        selectedDistance.append(currentDistance)
                        if toPrint:
                            print("current selectedPaths:", selectedPaths)
                            print("current selectedDistance:", selectedDistance)

        else:
            for nextEdge in digraph.get_edges_for_node(lastNode):
                nextNode = nextEdge.get_destination()

                if nextNode not in tmpPath:
                    nextPath = tmpPath + [nextNode]

                    pathQueue.append(nextPath)

    if len(selectedPaths) != 0:
        result = []
        for node in selectedPaths[-1]:
            result.append(node.get_name())
        return result

    else:
        raise ValueError("No such path")

#graph = load_map("mit_map.txt")
#
#result = directed_dfs(graph, "32", "56", 200, 0, True)
#
#print(result)

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


if __name__ == "__main__":
    unittest.main()
