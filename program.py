from typing import Optional
from graph_interfaces import IGraph, IVertex
from graph_impl import Graph

def read_graph(file_path: str) -> IGraph:  
    """
    Reads a CSV graph definition file and constructs a Graph object.
    Each line should be: source,destination,highway_name,distance
    """
    graph = Graph()
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()[1:]  # Skip the header line

            for line in lines:
                source, destination, highway, distance = line.strip().split(",")

                # Add vertices (if not already in graph)
                graph.add_vertex(source)
                graph.add_vertex(destination)

                # Add edge (bi-directional)
                graph.add_edge(highway, source, destination)
    except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            exit(1)
    except Exception as e:
            print(f"Error reading file '{file_path}': {e}")
            exit(1)

    return graph

def print_dfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Performs and prints a Depth-First Search traversal."""
    visited = set()

    def dfs(vertex: IVertex) -> None:
        print(vertex.get_name())
        visited.add(vertex.get_name())
        for edge in vertex.get_edges():
            neighbor = edge.get_destination()
            if neighbor.get_name() not in visited:
                dfs(neighbor)

    print("\nDFS Traversal:")
    dfs(start_vertex)

def print_bfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Performs and prints a Breadth-First Search traversal."""
    from collections import deque

    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex.get_name())

    print("\nBFS Traversal:")
    while queue:
        current = queue.popleft()
        print(current.get_name())
        for edge in current.get_edges():
            neighbor = edge.get_destination()
            if neighbor.get_name() not in visited:
                visited.add(neighbor.get_name())
                queue.append(neighbor)


def main() -> None:
    graph: IGraph = read_graph("graph.txt")
    start_vertex_name: str  = input("Enter the start vertex name: ")

    # Find the start vertex object
    start_vertex: Optional[IVertex]= next((v for v in graph.get_vertices() if v.get_name() == start_vertex_name), None)

    if start_vertex is None:
        print("Start vertex not found")
        return
    
    print_dfs(graph, start_vertex)
    print_bfs(graph, start_vertex)


if __name__ == "__main__":
    main()