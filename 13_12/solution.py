import json
def get_data():
    with open('input', 'r') as f:
        data = f.read().strip()
    return data

def parse_data(data):
    pairs = data.split('\n\n')
    return [[json.loads(line) for line in pair.split('\n')] for pair in pairs]

def compare_packets(packet_1, packet_2):
    for part_1, part_2 in zip(packet_1, packet_2):
        if isinstance(part_1, int) and isinstance(part_2, int):
            if part_2 == part_1:
                continue
            else:
                return part_1 < part_2
        else:
            if isinstance(part_1, int):
                part_1 = [part_1]
            if isinstance(part_2, int):
                part_2 = [part_2]
            x = compare_packets(part_1, part_2)
            if isinstance(x, bool):
                return x
    if len(packet_1) == len(packet_2):
        return
    else:
        return len(packet_1) < len(packet_2)

def get_valid_indices(parsed_data):
    return [v+1 for v, pair in enumerate(parsed_data) if compare_packets(*pair)]

def get_solution_1(data):
    parsed_data = parse_data(data)
    valid_indices = get_valid_indices(parsed_data)
    return sum(valid_indices)

def get_solution_2(data):
    pass

if __name__ == "__main__":
    input_data = get_data()
    solution_1 = get_solution_1(input_data)
    print("Solution 1:", solution_1)
    # solution_2 = get_solution_2(input_data)
    # print("Solution 2:", solution_2)