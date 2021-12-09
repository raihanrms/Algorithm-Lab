#include<iostream>

using namespace std;

// Number of vertices in the graph
const int V=6;

// Function to find the vertex with minimum key value
int min_key(int key[], bool visited[]){
    int min = 999, min_index; // infinite value
    for (int v = 0; v < V; v++){
        if (visited[v] == false && key[v] < min){
            // vertex not visited
            min = key[v];
            min_index = v;
        }
    }
    return min_index;
}

// function for printing the final mst stored in parent[]
int printMST(int parent[], int cost[V][V]){
    int minCost = 0;
    cout << "Edge \t Weight\n";
    for (int i = 1; i < V; i++){
        cout<<parent[i]<<" - "<<i<<" \t"<<cost[i][parent[i]]<<" \n";
        minCost += cost[i][parent[i]];
    }
    cout<<"Total cost is: "<<minCost;
}

// function to find the mst using adajency cost matrix representation
void findMST(int cost[V][V]){
    int parent[V], key[V];
    bool visited[V];

    // start the array
    for (int i = 0; i < V; i++){
        key[i] = 999;
        visited[i] = false;
        parent[i] = -1;
    }
    // include 1st vertex in mst and set it to 0
    key[0] = 0;
    // 1st node is always root
    parent[0] = -1;

    // mst will have maximum V-1 vertices
    for (int x = 0; x < V-1; x++){
        // find min key vertex from the set of vertices, not yet in mst
        int u = min_key(key, visited);

        // min key vertex to the mst
        visited[u] = true;

        // update key and parent array
        for (int v = 0; v < V; v++){
            // cost[u][v] is non zero only for adjacent vertices of u
            // visited[v] is false for vertices not yet included in MST
            // key[] gets updated only if cost[u][v] is smaller than key[v]
            if (cost[u][v] != 0 && visited[v] == false && cost[u][v] < key[v]){
                parent[v] = u;
                key[v] = cost[u][v];
            }
        }
    }
    // print the final mst
    printMST(parent, cost);
}

// main function
int main(){
    int cost[V][V];
    cout<<"Enter the vertices for a graph with 6 vertices";
    for (int i=0; i<V; i++){
        for (int j=0; j<V; j++){
            cin>>cost[i][j];
        }
    }
    findMST(cost);
    return 0;
}


// Graph with 6 vertices
// 0 4 0 0 0 2
// 4 0 6 0 0 3
// 0 6 0 3 0 1
// 0 0 3 0 2 0
// 0 0 0 2 0 4
// 2 3 1 0 4 0

// Edge    Weight
// 5 - 1   3
// 5 - 2   1
// 2 - 3   3
// 3 - 4   2
// 0 - 5   2

// Total cost is: 11

