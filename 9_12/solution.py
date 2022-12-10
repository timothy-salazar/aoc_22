
def get_data():
    with open('input', 'r') as f:
        data = f.read().strip().split('\n')
    return data

def update_tail(x_head, y_head, x_tail, y_tail):
    same_row = x_head == x_tail
    same_col = y_head == y_tail
    sproing = lambda head, tail: tail + ((head - tail) / abs(head - tail))
    if (abs(x_head - x_tail) < 2) and (abs(y_head - y_tail) < 2):
        return x_tail, y_tail
    if not same_row:
        x_tail = sproing(x_head, x_tail)
    if not same_col:
        y_tail = sproing(y_head, y_tail)
    return x_tail, y_tail

def update_head(x, y, d):
    if d == 'U':
        y += 1
    if d == 'D':
        y -= 1
    if d == 'R':
        x += 1
    if d == 'L':
        x -= 1
    return x, y

def get_solution_1(data):
    x_head, y_head, x_tail, y_tail = 0, 0, 0, 0
    tail_visited = {(0, 0)}
    for line in data:
        direction, steps = line.strip().split()
        for i in range(int(steps)):
            x_head, y_head = update_head(x_head, y_head, direction)
            x_tail, y_tail = update_tail(x_head, y_head, x_tail, y_tail)
            tail_visited.add((x_tail, y_tail))
    return len(tail_visited)

def update_rope(rope, direction):
    x_head, y_head = rope[0]
    rope[0] = update_head(x_head, y_head, direction)
    for i in range(len(rope)-1):
        x_head, y_head, x_tail, y_tail = *rope[i], *rope[i+1]
        x_tail, y_tail = update_tail(x_head, y_head, x_tail, y_tail)
        rope[i+1] = (x_tail, y_tail)
    return rope

def get_solution_2(data):
    rope = [[0, 0]]*10
    tail_visited = {(0, 0)}
    for line in data:
        direction, steps = line.strip().split()
        for i in range(int(steps)):
            update_rope(rope, direction)
            tail_visited.add(rope[-1])
    return len(tail_visited)


if __name__ == "__main__":
    solution_data = get_data()
    print('solution 1:', get_solution_1(solution_data))
    print('solution 2:', get_solution_2(solution_data))