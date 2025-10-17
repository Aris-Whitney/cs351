from graph_interfaces import IEdge, IGraph, IVertex
from typing import List, Optional

# Implementation definitions
# You should implement the bodies of the methods required by the interface protocols.


class Edge(IEdge):
    """Represents a connection between two vertices."""
    def __init__(self, name: str, destination: "Vertex") -> None:
        self._name = name
        self._destination = destination

    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str) -> None:
        self._name = name

    def get_destination(self) -> "Vertex":
        return self._destination
    
class Vertex(IVertex):
    """Represents a vertex in the graph."""
    def __init__(self, name: str) -> None:
        self._name = name
        self._edges: List[Edge] = []
        self._visited: bool = False

    def get_name(self) -> str:
        return self._name

    def get_edges(self) -> List[Edge]:
        return self._edges

    def add_edge(self, edge: Edge) -> None:
        self._edges.append(edge)

    def remove_edge(self, edge_name: str) -> None:
        self._edges = [e for e in self._edges if e.get_name() != edge_name]

    def set_visited(self, visited: bool) -> None:
        self._visited = visited

    def is_visited(self) -> bool:
        return self._visited
    
class Graph(IGraph):
    """Represents the entire graph, managing vertices and edges."""
    def __init__(self) -> None:
        self._vertices: List[Vertex] = []

    def add_vertex(self, name: str) -> None:
        # Prevent duplicates
        if not any(v.get_name() == name for v in self._vertices):
            self._vertices.append(Vertex(name))

    def add_edge(self, name: str, from_vertex_name: str, to_vertex_name: str) -> None:
        # Find or create 'from' vertex
        from_vertex: Optional[Vertex] = next((v for v in self._vertices if v.get_name() == from_vertex_name), None)
        to_vertex: Optional[Vertex] = next((v for v in self._vertices if v.get_name() == to_vertex_name), None)

        if from_vertex is None or to_vertex is None:
            raise ValueError(f"Cannot create edge '{name}' because one or both vertices do not exist.")

        # Add the edge in one direction for directed graph
        from_vertex.add_edge(Edge(name, to_vertex))

    def remove_vertex(self, vertex_name: str) -> None:
        self._vertices = [v for v in self._vertices if v.get_name() != vertex_name]
        for v in self._vertices:
            v.remove_edge(vertex_name)

    def remove_edge(self, edge_name: str) -> None:
        for v in self._vertices:
            v.remove_edge(edge_name)

    def get_vertices(self) -> List[Vertex]:
        return self._vertices

    def get_edges(self) -> List[Edge]:
        edges: List[Edge] = []
        for v in self._vertices:
            edges.extend(v.get_edges())
        return edges


