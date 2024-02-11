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

def get_best_path_bfs(digraph, src, dest, toPrint=False):
    path = {}
    path[(src, dest, "total")] = None
    path[(src, dest, "outdoor")] = None

    pathToDestQueue = []
    shortestPathTotalQueue = []
    shortestPathOutdoorQueue = []

    initPath = [src]
    pathQueue = [initPath]

    while len(pathQueue) != 0:
        # Get and remove oldest element from pathQueue
        tmpPath = pathQueue.pop(0)

        lastNode = tmpPath[-1]

        if lastNode == dest:
            pathToDestQueue.append(tmpPath)
            tmp_total_dist, tmp_outdoor_dist = 0, 0

            # get distance of each path inside tmpPath and increment them while tmp distance is shorter than current shortest distance
            if (path[(src, dest, "total")] == None) and (path[(src, dest, "outdoor")] == None):
                for i in range(len(tmpPath) - 1):
                    tmp_total_dist += int(digraph.get_edge(tmpPath[i], tmpPath[i + 1]).get_total_distance())
                    tmp_outdoor_dist += int(digraph.get_edge(tmpPath[i], tmpPath[i + 1]).get_outdoor_distance())

                path[(src, dest, "total")] = tmp_total_dist
                path[(src, dest, "outdoor")] = tmp_outdoor_dist

                shortestPathTotalLen = len(tmpPath)
                shortestPathOutdoorLen = len(tmpPath)

                shortestPathTotalQueue.append(tmpPath)
                shortestPathOutdoorQueue.append(tmpPath)

                if toPrint:
                    print("current total dist:", tmp_total_dist)
                    print("current outdoor dist:", tmp_outdoor_dist)

            else:
                # total
                tmp = False
                for i in range(len(tmpPath) - 1):
                    if i == len(tmpPath) - 2:
                        tmp = True
                    tmp_total_dist += int(digraph.get_edge(tmpPath[i], tmpPath[i + 1]).get_total_distance())

                    if tmp_total_dist < path[(src, dest, "total")]:
                        continue
                    else:
                        break

                if tmp:
                    if tmp_total_dist == path[(src, dest, "total")]:
                        if len(tmpPath) > shortestPathTotalLen:
                            break

                        else:
                            shortestPathTotalQueue.append(tmpPath)

                    elif tmp_total_dist < path[(src, dest, "total")]:
                        path[(src, dest, "total")] = tmp_total_dist
                        if toPrint:
                            print("current total dist:", tmp_total_dist)
                        shortestPathTotalQueue.append(tmpPath)

                # outdoor
                tmp = False
                for i in range(len(tmpPath) - 1):
                    if i == len(tmpPath) - 2:
                        tmp = True
                    tmp_outdoor_dist += int(digraph.get_edge(tmpPath[i], tmpPath[i + 1]).get_outdoor_distance())

                    if tmp_outdoor_dist < path[(src, dest, "outdoor")]:
                        continue
                    else:
                        break

                if tmp:
                    if tmp_outdoor_dist == path[(src, dest, "outdoor")]:
                        if len(tmpPath) > shortestPathOutdoorLen:
                            break

                        else:
                            shortestPathOutdoorQueue.append(tmpPath)
                    elif tmp_outdoor_dist <= path[(src, dest, "outdoor")]:
                        path[(src, dest, "outdoor")] = tmp_outdoor_dist
                        if toPrint:
                            print("current outdoor dist:", tmp_outdoor_dist)
                        shortestPathOutdoorQueue.append(tmpPath)

        # if not at goal
        for nextEdge in graph.get_edges_for_node(lastNode):
            # nextEdge is WeightedEdge
            # if toPrint:
            #     print("nextEdge :", nextEdge)

            nextNode = nextEdge.get_destination()
            # if toPrint:
            #     print("nextNode :", nextNode)

            if nextNode not in tmpPath:
                nextPath = tmpPath + [nextNode]
                # nextPath: [src, nextNode]
                pathQueue.append(nextPath)
                # if toPrint:
                #     print("pathQueue :", pathQueue)

    return path[(src, dest, "total")], path[(src, dest, "outdoor")], shortestPathTotalQueue, shortestPathOutdoorQueue

graph = load_map("mit_map.txt")

src = graph.get_node("32")
dest = graph.get_node("10")

# src = graph.get_node("48")
# dest = graph.get_node("50")

test = get_best_path_bfs(graph, src, dest, True)

def printResult(result):
    """
    1. shortest path total value
    2. shortest path outdoor value
    3. shortest path total queue
    4. shortest path outdoor queue
    """
    print("shortest path total value:", result[0])
    print("shortest path outdoor value:", result[1])
    for path in result[2]:
        print("shortest path total:", path)
    for path in result[3]:
        print("shortest path outdoor:", path)

printResult(test)
