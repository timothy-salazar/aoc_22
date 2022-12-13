from solution import parse_data, compare_packets, get_valid_indices, get_solution_1
from test_input import input_1, parsed_1, expected_1

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