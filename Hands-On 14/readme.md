### Name: Prathamesh Patil  
### Student ID: `1002233913`

## Overview
This repository contains implementations for the following algorithms:
1. **Dijkstra's Algorithm**
2. **Bellman-Ford Algorithm**
3. **Floyd-Warshall Algorithm**

## Algorithms

### 1. Dijkstra's Algorithm
- **Graph Representation**: Adjacency list, with nodes mapping to neighbors and weights.
- **Functionality**: Finds the shortest path from a single source node to all other nodes in a graph with non-negative edge weights.
- **Features**:
  - Implements a priority queue using a min-heap.
  - Supports finding the shortest distance to a specific end node.

---

### 2. Bellman-Ford Algorithm
- **Input**: A graph represented as a list of edges in the form `(u, v, weight)`.
- **Methodology**:
  - Iteratively relax edges to compute the shortest paths from a single source to all other nodes.
  - Detects negative-weight cycles.
- **Output**:
  - Shortest distances to all nodes or a warning if a negative-weight cycle is present.
  - Option to reconstruct the shortest path using predecessors.

---

### 3. Floyd-Warshall Algorithm
- **Graph Representation**: Adjacency matrix, with distances between every pair of nodes.
- **Functionality**: Computes the shortest paths between all pairs of nodes.
- **Features**:
  - Updates the adjacency matrix in-place using dynamic programming.
  - Handles negative weights but does not detect negative-weight cycles.
