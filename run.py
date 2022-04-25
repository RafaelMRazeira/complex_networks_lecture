from graph import Graphs

Graph = Graphs()

complete_graph = Graph.create_complete_graph(5)
print(complete_graph.edges())

chain_graph = Graph.create_circular_graph(5)
print(chain_graph.edges())


G = Graph.create_k_neighbor_circular_graph(10, 1)

Graph.draw()
print(Graph.adjacency_matrix())
print(Graph.laplacian_matrix())
