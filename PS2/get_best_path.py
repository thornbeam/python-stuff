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

def get_best_path(digraph, start, end, max_dist, max_dist_outdoors, toPrint=False):
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
    startNode = digraph.get_node(start)
    endNode = digraph.get_node(end)

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
                        if total_dist <= max_dist and total_dist_outdoors <= max_dist_outdoors:
                            total_dist += int(digraph.get_edge(tmpPath[i], tmpPath[i+1]).get_total_distance())
                            total_dist_outdoors += int(digraph.get_edge(tmpPath[i], tmpPath[i+1]).get_outdoor_distance())

                        else:
                            # break forloop
                            breakForLoop = True
                            break

                    else:

                        if total_dist <= prevTotalDist and total_dist <= max_dist and total_dist_outdoors <= max_dist_outdoors:
                            total_dist += int(digraph.get_edge(tmpPath[i], tmpPath[i+1]).get_total_distance())
                            total_dist_outdoors += int(digraph.get_edge(tmpPath[i], tmpPath[i+1]).get_outdoor_distance())

                        else:
                            # break forloop
                            breakForLoop = True
                            break
                else:
                    break


            if not breakForLoop:
                # due to last sequence of previous loop total_dist could be larger than max_dist
                if total_dist <= max_dist:
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
        return selectedPaths[-1]
    else:
        raise ValueError("No such path")

graph = load_map("mit_map.txt")

result = get_best_path(graph, "32", "10", 200, 100, True)

print(result)
