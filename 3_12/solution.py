from string import ascii_letters

def get_data():
    with open('input', 'r') as f:
        data = f.read()
    return data

def get_priority():
    priority = {i:j for i,j in zip(ascii_letters, range(1,53))}
    return priority

def get_solution_1(data, priority):
    priority_sum = 0
    for line in data.split('\n'):
        if not line:
            break
        x = len(line)//2
        comp_1 = set(line[:x])
        comp_2 = set(line[x:])
        diff = comp_1.intersection(comp_2)
        priority_sum += priority[diff.pop()]
    return priority_sum

def get_solution_2(data, priority):
    lines = [set(i) for i in data.split('\n')]
    priority_sum = 0
    for i in range(0, len(lines)-3, 3):
        elf_group = lines[i:i+3]
        x = elf_group[0].intersection(*elf_group[1:])
        priority_sum += priority[x.pop()]
    return priority_sum

if __name__ == "__main__":
    data = get_data()
    priority = get_priority()
    solution_1 = get_solution_1(data, priority)
    print("Solution 1:", solution_1)
    solution_2 = get_solution_2(data, priority)
    print("Solution 2:", solution_2)
