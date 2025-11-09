import streamlit as st

# Title
st.title("Graph Traversal: BFS and DFS")

# Define the graph
graph = {
    'A': ['B', 'D', 'E'],
    'B': ['C', 'G', 'H'],
    'C': [],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['G', 'F']
}

# BFS Function
def bfs(graph, start):
    visited = []
    queue = []
    visited.append(start)
    queue.append(start)
    order = []

    while queue:
        s = queue.pop(0)
        order.append(s)

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return order


# DFS Function
def dfs(graph, node, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    if node not in visited:
        visited.add(node)
        order.append(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited, order)
    return order


# User input
start_node = st.selectbox("Select starting node:", list(graph.keys()), index=0)

if st.button("Run BFS"):
    bfs_order = bfs(graph, start_node)
    st.success("BFS Traversal Order:")
    st.write(" → ".join(bfs_order))

if st.button("Run DFS"):
    dfs_order = dfs(graph, start_node)
    st.success("DFS Traversal Order:")
    st.write(" → ".join(dfs_order))
