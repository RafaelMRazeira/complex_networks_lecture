import numpy as np
import networkx as nx
from typing import Any
import matplotlib.pyplot as plt


class Graphs:
    def __init__(self) -> None:
        pass

    def create_complete_graph(self, nodes: int) -> Any:
        """Crete a complete graph with n nodes"""
        self.graph = nx.complete_graph(nodes)
        return self.graph

    def create_circular_graph(self, nodes: int) -> Any:
        """Return a chain from a nodes G"""
        self.graph = nx.cycle_graph(nodes)
        return self.graph

    def create_k_neighbor_circular_graph(self, nodes: int, k: int) -> Any:
        """Return a k-neighbor circular graph from a nodes G"""
        G = nx.Graph()
        G.add_nodes_from(range(nodes))
        edge_list = []
        for source_node in range(nodes):
            for target_node in range(source_node + 1, source_node + k + 1):
                edge_list.append((source_node, target_node % nodes))
        G.add_edges_from(edge_list)
        self.graph = G
        return self.graph

    def draw(self, graph=None):
        """Draw the graph"""
        graph = self.graph if graph is None else graph
        nx.draw(graph)
        plt.show()

    def adjacency_matrix(self, graph=None) -> np.ndarray:
        """Return the adjacency matrix of the graph"""
        graph = self.graph if graph is None else graph
        AM = nx.adjacency_matrix(graph)

        return np.array(AM.todense(), dtype="i2")

    def laplacian_matrix(self, graph=None) -> np.ndarray:
        """Return the laplacian matrix of the graph"""
        graph = self.graph if graph is None else graph
        LM = nx.laplacian_matrix(graph)
        return np.array(LM.todense(), dtype="i2")
