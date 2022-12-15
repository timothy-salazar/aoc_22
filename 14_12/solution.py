def get_data():
    with open('input.txt', 'r') as f:
        data = f.read().strip().split('\n')
    return data

def get_solution_1(data):
    return data[0]

def get_solution_2(data):
    return data[0]

if __name__ == "__main__":
    input_data = get_data()
    solution_1 = get_solution_1(input_data)
    print("Solution 1:", solution_1)
    solution_2 = get_solution_2(input_data)
    print("Solution 2:", solution_2)