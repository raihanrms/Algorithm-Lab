# to represent a graph class
class Graph:
    def __init__(self, vertices):
        # number of vertices
        self.V = vertices
        # to store graph in default dictionary
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # searching function done to find elements i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # function that does union of two sets x, y. Using union by rank
    def ApplyUnion(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # attach smaller rank tree under root of higher rank tree
        if rank[xroot] < rank[yroot]:
            parent[yroot] = xroot
            # of ranks are same, make one as root and increment its rank
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # kruskal's algorithm
    def KruskalsAlgo(self):
        # this will store the result of mst
        result = []

        # index variable to store edges and result
        i, e = 0, 0

        # Sort all the edges in non-decreasing order of weight
        # if not possible, make a copy of the graph
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        # create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # number of edges to be taken = V - 1
        while e < self.V - 1:
            # will pick the smallest edge and increment index for next iteration
            u, v, w = self.graph[i]
            i = i + 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            # if the edge doesn't cycle, append it in result and increment index
            # of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                # else disgard the edge
                self.ApplyUnion(parent, rank, x, y)
        for u, v, weight in result:
            print ("%d - %d: %d" % (u, v, weight))

g = Graph(6)
g.addEdge(0, 1, 4)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 2)
g.addEdge(1, 0, 4)
g.addEdge(2, 0, 4)
g.addEdge(2, 1, 2)
g.addEdge(2, 3, 3)
g.addEdge(2, 5, 2)
g.addEdge(2, 4, 4)
g.addEdge(3, 2, 3)
g.addEdge(3, 4, 3)
g.addEdge(4, 2, 4)
g.addEdge(4, 3, 3)
g.addEdge(5, 2, 2)
g.addEdge(5, 4, 3)
g.KruskalsAlgo()