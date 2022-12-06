
def get_data():
    with open('input', 'r') as f:
        data = f.read()
    return data


def marker_end_index(data, n):
    for i in range(len(data)):
        substring = data[i:i+n]
        if len(set(substring)) == n:
            return i+n

def get_solution_1(data):
    return marker_end_index(data, 4)

def get_solution_2(data):
    return marker_end_index(data, 14)

if __name__ == "__main__":
    solution_data = get_data()
    print('solution 1:', get_solution_1(solution_data))
    print('solution 2:', get_solution_2(solution_data))