from string import ascii_lowercase
import networkx as nx

def get_data():
    with open('input', 'r') as f:
        data = f.read().strip()
    return data

def data_to_heightmap(data):
    data = data.replace('S', 'a').replace('E', 'z')
    to_num = {i:v for v, i in enumerate(ascii_lowercase)}
    heightmap = [[to_num[char] for char in line] for line in data.split('\n')]
    return heightmap

def get_start_end(data):
    start_index = data.find('S')
    end_index = data.find('E')
    line_length = len(data.split('\n')[0]) + 1
    start = (start_index // line_length, start_index % line_length)
    end = (end_index // line_length, end_index % line_length)
    return start, end

def get_directions(heightmap, row, col):
    valid_directions = []
    current_val = heightmap[row][col]
    for r_inc, c_inc in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
        new_row = row + r_inc
        new_col = col + c_inc
        new_index = (new_row, new_col)
        # check to see if the point is over the edge of the map
        if not (0 <= new_row < len(heightmap)):
            continue
        if not (0 <= new_col < len(heightmap[0])):
            continue
        new_val = heightmap[new_row][new_col]
        not_too_steep = (new_val - current_val) <= 1
        if not_too_steep:
            valid_directions.append(new_index)
    return valid_directions

def make_graph(heightmap):
    G = nx.DiGraph()
    edges = set()
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            this_point = (i, j)
            directions = get_directions(heightmap, i, j)
            for other_point in directions:
                edges.add((this_point, other_point))
    G.add_edges_from(edges)
    return G

def get_low_points(heightmap):
    low_points = set()
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if heightmap[i][j] == 0:
                low_points.add((i,j))
    return low_points

def get_solution_1(data):
    start, end = get_start_end(data)
    heightmap = data_to_heightmap(data)
    G = make_graph(heightmap)
    return nx.shortest_path_length(G, start, end)

def get_solution_2(data):
    start, end = get_start_end(data)
    heightmap = data_to_heightmap(data)
    G = make_graph(heightmap)
    low_points = get_low_points(heightmap)
    path_dict = nx.shortest_path_length(G, target=end)
    reachable_low_points = low_points.intersection(path_dict.keys())
    path_lengths = [path_dict[i] for i in reachable_low_points]
    return min(path_lengths)

if __name__ == "__main__":
    input_data = get_data()
    solution_1 = get_solution_1(input_data)
    print("Solution 1:", solution_1)
    solution_2 = get_solution_2(input_data)
    print("Solution 2:", solution_2)
