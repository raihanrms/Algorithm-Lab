def primsAlgorithm(vertices):

    # Creating the adjacency Matrix with n x n dimensions filled with zeros, where n is the graph number of vertices:
    adjacencyMatrix = [[0 for column in range(vertices)] for row in range(vertices)]

    # Creating another adjacency Matrix for the Minimum Spanning Tree:
    mstMatrix = [[0 for column in range(vertices)] for row in range(vertices)]

    # Filling the adjacency matrix:
    for i in range(0,vertices):
        # Since the adjacency matrix is Symmetric we don't have to fill the whole matrix, only the upper half:
        for j in range(0+i,vertices):
            # Asking for the edges weights:
            adjacencyMatrix[i][j] = int(input('Enter the path weight between the vertices: ({}, {}):  '.format(i,j)))

            # Again, we use the Symmetric Matrix as an advantage:
            adjacencyMatrix[j][i] = adjacencyMatrix[i][j]

        # Defining a really big number:
    positiveInf = float('inf')

# This is a list showing which vertices are already selected, so we don't pick the same vertex twice and we can actually know when stop looking
    selectedVertices = [False for vertex in range(vertices)]

# While there are vertices that are not included in the MST, keep looking:
    while(False in selectedVertices):
        # We use the big number we created before as the possible minimum weight
        minimum = positiveInf

        # The starting vertex
        start = 0

        # The ending vertex
        end = 0

        for i in range(0,vertices):
            # If the vertex is part of the MST, look its relationships
            if selectedVertices[i]:
                # Again, we use the Symmetric Matrix as an advantage:
                for j in range(0+i,vertices):
                    # If the vertex analyzed have a path to the ending vertex AND its not included in the MST to avoid cycles)
                    if (not selectedVertices[j] and adjacencyMatrix[i][j]>0):  
                        # If the weight path analyzed is less than the minimum of the MST
                        if adjacencyMatrix[i][j] < minimum:
                            # Defines the new minimum weight, the starting vertex and the ending vertex
                            minimum = adjacencyMatrix[i][j]
                            start, end = i, j
        
        # Since we added the ending vertex to the MST, it's already selected:
        selectedVertices[end] = True

        # Filling the MST Adjacency Matrix fields:
        mstMatrix[start][end] = minimum
        
        # Initially, the minimum will be Inf if the first vertex is not connected with itself, but really it must be 0:
        if minimum == positiveInf:
            mstMatrix[start][end] = 0
            
        # Symmetric matrix, remember
        mstMatrix[end][start] = mstMatrix[start][end]

    # Show off:
    print(mstMatrix)
    
    # Here the function ends
#Call to the function:
primsAlgorithm(int(input('Enter the vertices number: ')))