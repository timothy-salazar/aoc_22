from test.test_inputs import input_1, expected_endpoints, \
    expected_line_points, expected_point_set, expected_sand_progression
from solution import str_to_endpoints, points_in_line, get_point_set, \
    get_abyss_level, move_sand, get_solution_1, get_solution_2

def test_str_to_endpoints():
    for line, expected in zip(input_1.split('\n'), expected_endpoints):
        endpoints = str_to_endpoints(line)
        assert endpoints == expected

def test_points_in_line():
    for endpoints, point_set in expected_line_points.items():
        point_1, point_2 = endpoints
        assert points_in_line(point_1, point_2) == point_set

def test_get_point_set():
    assert get_point_set(input_1.split('\n')) == expected_point_set

def test_get_abyss_level():
    assert get_abyss_level(expected_point_set) == 9

def test_progression():
    last_value = 0
    stone_set = get_point_set(input_1.split('\n'))
    point_set = stone_set.copy()
    for num, expected in expected_sand_progression.items():
        for i in range(num - last_value):
            point_set = move_sand(point_set)
        assert point_set.difference(stone_set) == expected
        last_value = num
    # any additional sand added should fall into the abyss, so the value of
    # sand_set shouldn't change
    sand_set = move_sand(point_set).difference(stone_set)
    assert sand_set == expected_sand_progression[24]

def test_solution_1():
    assert get_solution_1(input_1.split('\n')) == 24

# Part 2 tests

def test_new_floor_level():
    assert get_abyss_level(expected_point_set) + 2 == 11

def test_solution_2():
    assert get_solution_2(input_1.split('\n')) == 93