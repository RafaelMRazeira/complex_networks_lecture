import pytest
from graph import Graphs


@pytest.mark.parametrize(
    "nodes, expected",
    [
        (0, 0),
        (1, 0),
        (2, 1),
        (3, 3),
        (4, 6),
        (5, 10),
        (6, 15),
        (7, 21),
        (8, 28),
        (9, 36),
        (10, 45),
    ],
)
def test_create_complete_graph(nodes, expected):
    """Test the create_complete_graph function"""
    graph = Graphs()
    complete_graph = graph.create_complete_graph(nodes)
    assert len(complete_graph.edges()) == expected


@pytest.mark.parametrize(
    "nodes, expected",
    [
        (1, 1),
        (2, 1),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    ],
)
def test_create_circular_graph(nodes, expected):
    """Test the create_circular_graph function"""
    graph = Graphs()
    circular_graph = graph.create_circular_graph(nodes)
    assert len(circular_graph.edges()) == expected


@pytest.mark.parametrize(
    "nodes, k, expected",
    [
        (1, 1, 1),
        (2, 1, 1),
        (3, 1, 3),
        (4, 1, 4),
        (5, 1, 5),
        (6, 1, 6),
        (7, 1, 7),
        (8, 1, 8),
        (9, 1, 9),
        (10, 1, 10),
    ],
)
def test_create_k_neighbor_circular_graph(nodes, k, expected):
    """Test the create_k_neighbor_circular_graph function"""
    graph = Graphs()
    G = graph.create_k_neighbor_circular_graph(nodes, k)
    assert len(G.edges()) == expected
