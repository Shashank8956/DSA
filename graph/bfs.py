# Link to GFG problem
# https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bfs_of_graph

# BFS uses Queue and Visited Array

# Function to return Breadth First Traversal of given graph.
# V == Number of nodes
# adj == Adjacency list
def bfsOfGraph(self, V, adj):
    bfsResult = []       # Stores the BFS traversal result
    visited = [0]*V      # Visited list of size V initialized to 0
    visited[0] = 1       # Mark starting node, 0, as visited
    q = [0]              # Add starting node, 0, to the queue
    
    # While the queue is not empty (0)
    while(len(q)):
        node = q[0]                   # Take the first element out of the queue to process it
        del q[0]                      # Remove/Pop the first element from the queue
        bfsResult.append(node)        # Add this extracted element to the result
        
        # For each node adjacent to the extracted node
        for newNode in adj[node]:     # Extract each node from the adj list
            if(not visited[newNode]): # If this new extracted node has not been visited
                visited[newNode] = 1  # Mark it as visited
                q.append(newNode)     # Add it to the queue
                
    return bfsResult     # Return the result