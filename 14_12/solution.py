ENTRY_POINT = (500, 0)

def get_data():
    with open('input.txt', 'r') as f:
        data = f.read().strip().split('\n')
    return data

def get_point_set(data: list):
    """ Input:
            data: list - a list of strings in which each string is a single
                line from the input file.
        Output:
            point_set: set - the set of all points occupied by rock
    """
    point_set = set()
    for line in data:
        endpoints = str_to_endpoints(line)
        for point_1, point_2 in zip(endpoints[:-1], endpoints[1:]):
            point_set.update(points_in_line(point_1, point_2))
    return point_set 

def str_to_endpoints(line: str):
    """ Input:
            line: str - one line of the input file
        Output:
            endpoints: list of lists in which each element is a tuple
                representing a single point
    """
    point_strings = line.split(' -> ')
    endpoints = [tuple([int(point) for point in point_string.split(',')])
                 for point_string in point_strings]
    return endpoints

def points_in_line(point_1: int, point_2: int):
    """ Input:
            point_1, point_2: int - the endpoints of a line
        Output:
            line_points: set - the set of points that make up the line whose
                endpoints are point_1 and point_2
    """
    get_range = lambda p1, p2: range(min(p1, p2), max(p1, p2)+1)
    if point_1[0] == point_2[0]:
        return {(point_1[0], i) for i in get_range(point_1[1], point_2[1])}
    else:
        return {(i, point_1[1]) for i in get_range(point_1[0], point_2[0])}

def get_abyss_level(rock_set: set):
    """ Input:
            rock_set: set - the set of all points occupied by rock.
        Output:
            abyssal_y: the y value of the lowest point occupied by any rock.
                Any sand falling below this y value will fall into the abyss.
    """
    abyssal_y = max(rock_set, key=lambda x: x[1])[1]
    return abyssal_y

def move_sand(blocked_points):
    """ Input:
            blocked_points: set - the set of all points occupied by
                either rock or units of sand
        Output:
            blocked_points: set - the set of all occupied points, updated to
                include the position of an additional unit of sand after it
                has come to rest.
                If the additional unit of sand falls into the bottomless abyss,
                falling forever into the inchoate void, then blocked_points
                will be unchanged.
    """
    sand_x = 500
    sand_y = 0
    abyssal_y = get_abyss_level(blocked_points)
    while True:
        if sand_y > abyssal_y:
            return blocked_points
        if (sand_x, sand_y + 1) not in blocked_points:
            sand_y += 1
            continue
        elif (sand_x - 1, sand_y + 1) not in blocked_points:
            sand_x, sand_y = sand_x - 1, sand_y + 1
            continue
        elif (sand_x + 1, sand_y + 1) not in blocked_points:
            sand_x, sand_y = sand_x + 1, sand_y + 1
            continue
        else:
            blocked_points.add((sand_x, sand_y))
            return blocked_points

def get_solution_1(data):
    last_value = 0
    stone_set = get_point_set(data)
    point_set = stone_set.copy()
    while True:
        point_set = move_sand(point_set)
        this_value = len(point_set.difference(stone_set))
        if this_value == last_value:
            return this_value
        else:
            last_value = this_value


def get_solution_2(data):
    stone_set = get_point_set(data)
    actual_floor_level = get_abyss_level(stone_set) + 2
    return data[0][0]

if __name__ == "__main__":
    input_data = get_data()
    solution_1 = get_solution_1(input_data)
    print("Solution 1:", solution_1)
    solution_2 = get_solution_2(input_data)
    print("Solution 2:", solution_2)