import numpy as np
from itertools import product

def get_data():
    with open('input', 'r') as f:
        data = f.read().strip()
    return data

def data_to_array(data):
    trees = np.array([[int(i) for i in line]
                      for line in data.split('\n') if line])
    return trees




def is_hidden(arr, i, j, verbose=False):
    val = arr[i, j]
    row = arr[i]
    col = arr[:, j]
    d1 = (row[:j] >= val).any()
    d2 = (row[j+1:] >= val).any()
    d3 = (col[:i] >= val).any()
    d4 = (col[i+1:] >= val).any()
    if verbose:
        print(f'd1: {d1} d2: {d2} d3: {d3} d4: {d4}')
    if d1 and d2 and d3 and d4:
        return True
    return False

def scenic_score(arr, i, j):
    val = arr[i, j]
    row = arr[i]
    col = arr[:, j]
    directions = [
        row[:j][::-1],
        row[j+1:],
        col[:i][::-1],
        col[i+1:]
    ]
    score = 1
    for direction in directions:
        for v, tree in enumerate(direction):
            if (tree >= val) or (v == (len(direction) - 1)):
                score = score * (1+v)
                break
    return score

def get_solution_1(arr):
    rows, cols = arr.shape
    hidden_trees = [is_hidden(arr, pair[0], pair[1]) 
                    for pair in product(range(rows), range(cols))]
    return (rows*cols) - sum(hidden_trees)


def get_solution_2(arr):
    rows, cols = arr.shape
    scenic_scores = [scenic_score(arr, pair[0], pair[1]) 
                    for pair in product(range(rows), range(cols))]
    return max(scenic_scores)

def get_test_arr():
    arr = np.array([
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0]
    ])
    return arr

def test_pt_1():
    arr = get_test_arr()
    assert is_hidden(arr, 1, 1) == False
    assert is_hidden(arr, 1, 2) == False
    assert is_hidden(arr, 1, 3) == True
    assert is_hidden(arr, 2, 1) == False
    assert is_hidden(arr, 2, 2) == True
    assert is_hidden(arr, 2, 3) == False
    assert is_hidden(arr, 3, 1) == True
    assert is_hidden(arr, 3, 2) == False
    assert is_hidden(arr, 3, 3) == True
    assert get_solution_1(arr) == 21

def test_pt_2():
    arr = get_test_arr()
    assert scenic_score(arr, 1, 2) == 4
    assert scenic_score(arr, 3, 2) == 8


if __name__ == "__main__":
    solution_data = get_data()
    tree_array = data_to_array(solution_data)
    print('solution 1:', get_solution_1(tree_array))
    print('solution 2:', get_solution_2(tree_array))

    # np.rot90