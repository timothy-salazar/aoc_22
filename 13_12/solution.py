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

def flatten_data(parsed_data):
    flattened = [packet for pair in parsed_data for packet in pair]
    return flattened

def crude_sort(packets):
    for i in range(len(packets)):
        j = i
        while j > 0 and compare_packets(packets[j], packets[j-1]):
            packets[j], packets[j-1] = packets[j-1], packets[j]
            j -= 1
    return packets


def get_valid_indices(parsed_data):
    return [v+1 for v, pair in enumerate(parsed_data) if compare_packets(*pair)]

def get_solution_1(data):
    parsed_data = parse_data(data)
    valid_indices = get_valid_indices(parsed_data)
    return sum(valid_indices)

def get_solution_2(data):
    key_1 = [[2]]
    key_2 = [[6]]
    parsed_data = parse_data(data)
    packets = flatten_data(parsed_data)
    packets += [key_1, key_2]
    packets = crude_sort(packets)
    index_1 = packets.index(key_1) + 1
    index_2 = packets.index(key_2) + 1
    return index_1 * index_2


if __name__ == "__main__":
    input_data = get_data()
    solution_1 = get_solution_1(input_data)
    print("Solution 1:", solution_1)
    solution_2 = get_solution_2(input_data)
    print("Solution 2:", solution_2)