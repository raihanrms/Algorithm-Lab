class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # searching
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def ApplyUnion(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # kruskal's algorithm
    def KruskalsAlgo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
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



