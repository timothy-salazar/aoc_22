from test_inputs import test_input_1
from solution import get_start_end, data_to_heightmap, make_graph, get_low_points
import networkx as nx

# minimal tests, I know - I feel bad
def test_1():
    start, end = get_start_end(test_input_1)
    heightmap = data_to_heightmap(test_input_1)
    G = make_graph(heightmap)
    assert nx.shortest_path_length(G, start, end) == 31

def test_2():
    start, end = get_start_end(test_input_1)
    heightmap = data_to_heightmap(test_input_1)
    G = make_graph(heightmap)
    low_points = get_low_points(heightmap)
    path_dict = nx.shortest_path_length(G, target=end)
    reachable_low_points = low_points.intersection(path_dict.keys())
    path_lengths = [path_dict[i] for i in reachable_low_points]
    assert min(path_lengths) == 29