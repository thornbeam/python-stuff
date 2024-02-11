class Node(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

class Edge(object):
    """src and dest are nodes"""
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return "{}->{}".format(self.src.getName(), self.dest.getName())

class Digraph(object):
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node not in self.edges:
            self.edges[node] = []

        else:
            raise ValueError("Duplicate node")


    def addEdge(self, edge):
        """Works only if nodes are already in self.edges"""
        src = edge.getSource()
        dest = edge.getDestination()

        if not (src in self.edges and dest in self.edges):
            raise ValueError("Node not in graph")
        self.edges[src].append(dest)

    def childrenOf(self, node):
        """ get list of destination's' from node """
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for i in self.edges:
            if i.getName() == name:
                return i

        raise NameError(name)

    def __str__(self):
        result = ""
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + "->" + dest.getName() + "\n"

        return result

class Graph(Digraph):
    """Makes digraph bidirectical"""

    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

def buildGraph(graphType):
    """graphType is a class: Digraph or Graph"""

    g = graphType()

    for name in ("A", "B", "C", "D", "E", "F", "G"):
        g.addNode(Node(name))

    g.addEdge(Edge(g.getNode("A"), g.getNode("B")))
    g.addEdge(Edge(g.getNode("A"), g.getNode("E")))
    g.addEdge(Edge(g.getNode("B"), g.getNode("F")))
    g.addEdge(Edge(g.getNode("C"), g.getNode("E")))
    g.addEdge(Edge(g.getNode("C"), g.getNode("G")))
    g.addEdge(Edge(g.getNode("D"), g.getNode("F")))
    g.addEdge(Edge(g.getNode("D"), g.getNode("G")))

    return g

graph = buildGraph(Graph)

print(graph)

def DFS(graph, start, end, path, shortest, toPrint=False):
    """
    Assumes graph is Digraph
    start and end are Node
    path and shortest are list of Nodes
    Returns the shortest path from start to end in graph
    """

    path = path + [start]

    if start == end:
        return path

    else:
        for node in graph.childrenOf(start):
            if node not in path:
                if shortest == None or len(path) < len(shortest):
                    newPath = DFS(graph, node, end, path, shortest, toPrint)

                    if newPath != None:
                        shortest = newPath
    return shortest

result = DFS(graph, graph.getNode("A"),graph.getNode("D"), [], None, True)

shortest = []
for n in result:
    shortest.append(n.getName())
print(shortest)
