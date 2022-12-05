
def get_data():
    with open('input', 'r') as f:
        data = f.read()
    return data.split('\n')[:-1]

def get_assignment_sets(data):
    assignment_boundaries = [[[int(k) for k in j.split('-')]
            for j in i.split(',')]
                for i in data]
    assignments = [[set(range(j[0], j[1]+1)) for j in i]
        for i in assignment_boundaries]
    return assignments

def get_solution_1(data):
    assignments = get_assignment_sets(data)
    subsets = 0
    for ass_pair in assignments:
        elf_1, elf_2 = ass_pair
        if (elf_1 <= elf_2) or (elf_2 <= elf_1):
            subsets += 1
    return subsets

def get_solution_2(data):
    assignments = get_assignment_sets(data)
    overlap = 0
    for ass_pair in assignments:
        elf_1, elf_2 = ass_pair
        if not elf_1.isdisjoint(elf_2):
            overlap += 1
    return overlap

if __name__ == "__main__":
    solution_data = get_data()
    solution_1 = get_solution_1(solution_data)
    print("Solution 1:", solution_1)
    solution_2 = get_solution_2(solution_data)
    print("Solution 2:", solution_2)
