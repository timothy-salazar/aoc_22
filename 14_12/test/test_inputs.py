input_1 = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''

expected_endpoints = [
    [(498, 4), (498, 6), (496, 6)],
    [(503, 4), (502, 4), (502, 9), (494, 9)]
]

expected_line_points = {
    ((498, 4), (498, 6)): {             # itty bitty vertical line segment
        (498, 6), (498, 5), (498, 4)
    },
    ((498, 6), (496, 6)): {             # medium horizontal line segment
        (496, 6), (497, 6), (498, 6),
    },
    ((503, 4), (502, 4)): {             # itty bitty horizontal line segment
        (502, 4), (503, 4),
    },
    ((502, 4), (502, 9)): {             # long vertical line segment
        (502, 9), (502, 8), (502, 7),
        (502, 6), (502, 5), (502, 4),
    },
    ((502, 9), (494, 9)):  {            # bottom line segment
        (494, 9), (495, 9), (496, 9),
        (497, 9), (498, 9), (499, 9),
        (500, 9), (501, 9), (502, 9),
    },
}

expected_point_set = {
    (494, 9), (495, 9), (496, 6), (496, 9), (497, 6),
    (497, 9), (498, 4), (498, 5), (498, 6), (498, 9),
    (499, 9), (500, 9), (501, 9), (502, 4), (502, 5),
    (502, 6), (502, 7), (502, 8), (502, 9), (503, 4),
}

expected_sand_progression = {
    1:{(500, 8)},
    2:{(499, 8), (500, 8)},
    5:{(499, 8), (498, 8), (501, 8), (500, 7), (500, 8)},
    22: {
        (499, 7), (500, 6), (500, 4), (501, 5), (501, 3),
        (497, 8), (500, 8), (499, 6), (498, 7), (501, 7),
        (500, 3), (499, 4), (500, 5), (499, 8), (501, 6),
        (500, 7), (499, 3), (499, 5), (501, 4), (498, 8),
        (501, 8), (500, 2)
    },
    24: {
        (499, 7), (500, 6), (500, 4), (501, 5), (501, 3),
        (497, 8), (500, 8), (499, 6), (498, 7), (501, 7),
        (500, 3), (497, 5), (499, 4), (500, 5), (499, 8),
        (501, 6), (500, 7), (499, 3), (499, 5), (501, 4),
        (495, 8), (498, 8), (501, 8), (500, 2)
    }
}


# Here's a lil' script I wrote to make getting examples for tests easier
import subprocess
def paste_to_set(char='o', offset=494):
    """ Input:
            char: str - the character we're interested in. If we want to know
                the set of points occupied by rocks, we'd use '#', if we
                want the set of points occupied by sand we'd use 'o'
            offset: int - an offset applied to x coordinates
        Output:
            char_points: set of tuples - the set of points represented by "char"
                characters
    """
    s = subprocess.run('pbpaste',
                       capture_output=True,
                       text=True,
                       check=True).stdout
    char_points = set()
    for y, line in enumerate(s.split('\n')):
        for x, i in enumerate(line):
            if i == char:
                char_points.add((x + offset, y))
    subprocess.run('pbcopy', input=repr(char_points), text=True, check=True)