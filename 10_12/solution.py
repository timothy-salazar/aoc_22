from collections.abc import Iterator

class ElfVM(Iterator):
    def __init__(self, data):
        # reversing this so we can use .pop().
        # we could use .pop(0), but it's less efficient and that bugs me a bit
        self.data = data[::-1]
        self.register = 1
        self.increment = None
        self.instruction = ''
        self.execution_time = 0

    def __next__(self):
        if self.instruction is None:
            raise StopIteration
        self.clock_cycle()
        return self.register

    def clock_cycle(self):
        if self.execution_time > 0:
            self.execution_time -= 1
        else:
            self.execute_instruction()
            return self.load_instruction()

    def load_instruction(self):
        if not self.data:
            self.instruction = None
            return
        self.instruction = self.data.pop()
        if self.instruction[:4] == 'noop':
            self.execution_time = 0
            self.increment = None
        elif self.instruction[:4] == 'addx':
            argument = self.instruction.split()[1]
            self.execution_time = 1
            self.increment = int(argument)

    def execute_instruction(self):
        if self.increment:
            self.register += self.increment

def get_data():
    with open('input', 'r') as f:
        data = f.read().strip().split('\n')
    return data

def get_signal_strength(vm, start, stop, step):
    signal_strength = [i*(v+1) for v, i in enumerate(vm)]
    return sum(signal_strength[slice(start, stop, step)])


def get_solution_1(data):
    vm = ElfVM(data)
    return get_signal_strength(vm, 19, 220, 40)


def get_solution_2(arr):
    pass



# def test_pt_1():
#     arr = get_test_arr()
#     assert is_hidden(arr, 1, 1) == False
#     assert is_hidden(arr, 1, 2) == False
#     assert is_hidden(arr, 1, 3) == True
#     assert is_hidden(arr, 2, 1) == False
#     assert is_hidden(arr, 2, 2) == True
#     assert is_hidden(arr, 2, 3) == False
#     assert is_hidden(arr, 3, 1) == True
#     assert is_hidden(arr, 3, 2) == False
#     assert is_hidden(arr, 3, 3) == True
#     assert get_solution_1(arr) == 21

# def test_pt_2():
#     arr = get_test_arr()
#     assert scenic_score(arr, 1, 2) == 4
#     assert scenic_score(arr, 3, 2) == 8


if __name__ == "__main__":
    
    solution_data = get_data()
    print('solution 1:', get_solution_1(solution_data))
    # print('solution 2:', get_solution_2(tree_array))
