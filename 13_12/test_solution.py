from solution import parse_data, compare_packets, get_valid_indices,\
     get_solution_1, get_solution_2, flatten_data, crude_sort
from test_input import input_1, parsed_1, expected_1, input_2
import json

# Part 1 tests
def test_parser():
    parsed_data = parse_data(input_1)
    assert parsed_data == parsed_1

def test_comparison():
    parsed_data = parse_data(input_1)
    for pair, expected in zip(parsed_data, expected_1):
        assert compare_packets(*pair) == expected

def test_valid_indices():
    parsed_data = parse_data(input_1)
    assert get_valid_indices(parsed_data) == [1, 2, 4, 6]

def test_solution_1():
    assert get_solution_1(input_1) == 13

# Part 2 tests
def test_flattener():
    parsed_data = parse_data(input_1)
    assert len(parsed_data) == 8
    flat = flatten_data(parsed_data)
    assert len(flat) == 16

def test_sort():
    parsed_data = parse_data(input_1)
    flat = flatten_data(parsed_data)
    flat += [[[2]], [[6]]]
    expected = [json.loads(line) for line in input_2.split('\n')]
    flat = crude_sort(flat)
    assert flat == expected
    assert flat.index([[2]]) + 1 == 10
    assert flat.index([[6]]) + 1 == 14

def test_solution_2():
    assert get_solution_2(input_1) == 140