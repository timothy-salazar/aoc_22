from collections.abc import Iterator

class ElfVM(Iterator):
    def __init__(self, data):
        # reversing this so we can use .pop().
        # we could use .pop(0), but it's less efficient and that bugs me a bit
        self.data = data[::-1]
        self.register = 1
        self.clock = 0
        self.increment = None
        self.instruction = ''
        self.execution_time = 0

    def __next__(self):
        if self.instruction is None:
            raise StopIteration
        self.clock_cycle()
        # if not self.clock_cycle():
            # self.execution_time = -1
            # return self.register
        return self.register

    def clock_cycle(self):
        if self.execution_time > 0:
            self.execution_time -= 1
            return True
        else:
            self.execute_instruction()
            return self.load_instruction()

    def load_instruction(self):
        if not self.data:
            self.instruction = None
            return False
        instruction = self.data.pop()
        self.instruction = instruction
        if instruction[:4] == 'noop':
            self.execution_time = 0
            self.increment = None
        elif instruction[:4] == 'addx':
            argument = instruction.split()[1]
            self.execution_time = 1
            self.increment = int(argument)
        return True

    def execute_instruction(self):
        if self.increment:
            self.register += self.increment



def get_data():
    with open('input', 'r') as f:
        data = f.read().strip().split('\n')
    return data


def get_solution_1(arr):
    pass


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
    pass
    # solution_data = get_data()
    # tree_array = data_to_array(solution_data)
    # print('solution 1:', get_solution_1(tree_array))
    # print('solution 2:', get_solution_2(tree_array))

    # np.rot90