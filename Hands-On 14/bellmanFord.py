def bellman_ford(edges, start_node):
    all_nodes = set()
    for from_node, to_node, weight in edges:
        all_nodes.add(from_node)
        all_nodes.add(to_node)
    
    shortest_distances = {node: float('inf') for node in all_nodes}
    path_predecessors = {node: None for node in all_nodes}
    shortest_distances[start_node] = 0

    for _ in range(len(all_nodes) - 1):
        for from_node, to_node, weight in edges:
            if shortest_distances[from_node] + weight < shortest_distances[to_node]:
                shortest_distances[to_node] = shortest_distances[from_node] + weight
                path_predecessors[to_node] = from_node

    for from_node, to_node, weight in edges:
        if shortest_distances[from_node] + weight < shortest_distances[to_node]:
            return shortest_distances, path_predecessors, True  # Negative cycle detected

    return shortest_distances, path_predecessors, False

def reconstruct_path(path_predecessors, start_node, end_node):
    path = []
    current_node = end_node
    while current_node is not None:
        path.append(current_node)
        current_node = path_predecessors[current_node]
    return path[::-1] if path and path[-1] == start_node else []

# Test cases from diagrams
test_cases = [
    {
        "edges": [
            ('s', 't', 6), ('s', 'y', 7), 
            ('t', 'x', 5), ('t', 'y', 8), ('t', 'z', -4), 
            ('y', 't', -3), ('y', 'x', 9), ('y', 'z', 2),
            ('z', 's', 7), ('z', 'x', 6),
            ('x', 'z', -2)
        ],
        "start_node": 's',
        "description": "Graph (a)"
    }
]

print("Bellman-Ford Algorithm Test Cases\n" + "=" * 40)
for i, test_case in enumerate(test_cases, 1):
    edges = test_case["edges"]
    start_node = test_case["start_node"]
    description = test_case["description"]

    print(f"\nTest Case {i}: {description}")
    print(f"Edges: {edges}")
    print(f"Start Node: {start_node}")

    shortest_distances, path_predecessors, has_negative_cycle = bellman_ford(edges, start_node)

    if has_negative_cycle:
        print("Result: Negative-weight cycle detected.")
    else:
        print(f"Shortest Distances: {shortest_distances}")
        print(f"Predecessors: {path_predecessors}")
        for node in shortest_distances:
            path = reconstruct_path(path_predecessors, start_node, node)
            print(f"Shortest Path to {node}: {path if path else 'No path exists'}")



# OUTPUT

# Bellman-Ford Algorithm Test Cases
# ========================================

# Test Case 1: Graph (a)
# Edges: [('s', 't', 6), ('s', 'y', 7), ('t', 'x', 5), ('t', 'y', 8), ('t', 'z', -4), ('y', 't', -3), ('y', 'x', 9), ('y', 'z', 2), ('z', 's', 7), ('z', 'x', 6), ('x', 'z', -2)]
# Start Node: s
# Shortest Distances: {'t': 4, 'z': 0, 'y': 7, 'x': 6, 's': 0}
# Predecessors: {'t': 'y', 'z': 't', 'y': 's', 'x': 'z', 's': None}
# Shortest Path to t: ['s', 'y', 't']
# Shortest Path to z: ['s', 'y', 't', 'z']
# Shortest Path to y: ['s', 'y']
# Shortest Path to x: ['s', 'y', 't', 'z', 'x']
# Shortest Path to s: ['s']