import re

def get_data():
    with open('input', 'r') as f:
        data = f.read()
    return data.split('\n')[:-1]

def split_data(data):
    for v, line in enumerate(data):
        if not line:
            return data[:v], data[v+1:]

def get_cargo(crates):
    extract_values = lambda line: [line[i] for i in range(1, 35, 4)]
    keys = extract_values(crates.pop())
    value_list = [extract_values(line) for line in crates]
    cargo = {key:[value[i] for value in value_list if value[i].strip()][::-1]
             for i, key in enumerate(keys)}
    return cargo


def get_solution_1(data):
    crates, moves = split_data(data)
    cargo = get_cargo(crates)
    get_moves = 'move (?P<num>[0-9]+) from (?P<orig>[0-9]+) to (?P<dest>[0-9]+)'
    for move in moves:
        m = re.match(get_moves, move)
        quant, orig, dest = m.groups()
        cargo[dest] += cargo[orig][-1*int(quant):][::-1]
        del cargo[orig][-1*int(quant):]
    return ''.join([v[-1] for v in cargo.values()])

def get_solution_2(data):
    crates, moves = split_data(data)
    cargo = get_cargo(crates)
    get_moves = 'move (?P<num>[0-9]+) from (?P<orig>[0-9]+) to (?P<dest>[0-9]+)'
    for move in moves:
        m = re.match(get_moves, move)
        quant, orig, dest = m.groups()
        cargo[dest] += cargo[orig][-1*int(quant):]
        del cargo[orig][-1*int(quant):]
    return ''.join([v[-1] for v in cargo.values()])

if __name__ == "__main__":
    solution_data = get_data()
    print('solution 1:', get_solution_1(solution_data))
    print('solution 2:', get_solution_2(solution_data))