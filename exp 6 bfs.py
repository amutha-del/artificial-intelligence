from collections import deque

def bfs(graph, start):
    visited = set()             # To keep track of visited nodes
    queue = deque([start])      # Initialize queue with the starting node

    print("BFS Traversal:")

    while queue:
        node = queue.popleft()  # Dequeue the next node

        if node not in visited:
            print(node, end=" ")
            visited.add(node)   # Mark the node as visited
            queue.extend(graph[node])  # Enqueue all unvisited neighbors

# Example Graph (as adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Start BFS from node 'A'
bfs(graph, 'A')
