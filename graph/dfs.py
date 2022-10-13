# Link to GFG problem
# https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=dfs_of_graph

# DFS uses Stack and Visited Array

# Main DFS Recursive function
# node == current node to be processed
# adj == Adjacency list
# visited == visited array of 0 and 1
# dfsResult == Final result of that will be passed
def dfs(self, node, adj, visited, dfsResult):
    visited[node] = 1                   # Mark the current node as visited
    dfsResult.append(node)              # Add the node to the final result
    
    # For each node adjacent to the current node
    for newNode in adj[node]:           # Extract each node from the adj list
        if(not visited[newNode]):       # If this new extracted node has not been visited
            self.dfs(newNode, adj, visited, dfsResult)   # Then recursively call the DFS function
    
# Function to return Depth First Traversal of given graph.
# V == Number of nodes
# adj == Adjacency list
def dfsOfGraph(self, V, adj):
    dfsResult = []       # Stores the BFS traversal result
    visited = [0]*V      # Visited list of size V initialized to 0
    startNode = 0        # Start/Root node of the dfs
    
    self.dfs(startNode, adj, visited, dfsResult)    # Begin dfs 
    return dfsResult     # Return the dfs travelsal result


# Below is the itterative version of DFS

# This solution will not work in GFG because it prints from right to left
# i.e., it first traverses the right branch and then the moves towards the left
# whereas GFG requires use to print from right to left
def dfsIterative(self, V, adj):                 
    dfsResult = []       # Stores the DFS traversal result
    visited = [0]*V      # Visited list of size V initialized to 0
    visited[0] = 1       # Mark 1st node, 0, as visited
    stack = []           # Create a stack
    stack.append(0)      # Add first node, 0, to the stack

    # While the stack is not empty (0)
    while (len(stack)):
        node = stack[-1]                # Take the top element out of the stack to process it
        stack.pop()                     # Remove/Pop the first element from the queue
        dfsResult.append(node)          # Add this extracted element to the result
        
        # For each node adjacent to the extracted node
        for newNode in adj[node]:
            if (not visited[newNode]):  # If this new extracted node has not been visited
                visited[newNode] = 1    # Then mark it as visited
                stack.append(newNode)   # And add it to the stack

    return dfsResult      # Return the dfs travelsal result