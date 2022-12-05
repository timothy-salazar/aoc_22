
def get_data():
    with open('input', 'r') as f:
        data = f.read()
    return data.split('\n')[:-1]

def get_cargo(data):
    extract_values = lambda line: [line[i] for i in range(1, 35, 4)]
    crates = data[:9]
    keys = extract_values(crates.pop())
    value_list = [extract_values(line) for line in crates]
    cargo = {key:[value[i] for value in value_list if value[i].strip()][::-1]
             for i, key in enumerate(keys)}
    return cargo

def get_solution_1(data):
    cargo = get_cargo(data)

def get_solution_2(data):
    pass

if __name__ == "__main__":
    solution_data = get_data()
    