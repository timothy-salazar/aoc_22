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

class Screen:
    def __init__(self, data, width=40, height=6):
        self.width = width
        self.crt_loc = [i for i in range(width)]*height
        self.pixels = ''
        self.vm = ElfVM(data)
        self.gen = self.get_gen()

    def __str__(self):
        return self.pixels

    def __next__(self):
        self.gen.__next__()

    def get_gen(self):
        # I broke this out into a generator function to allow easy testing
        for sprite_loc, current_pixel in zip(self.vm, self.crt_loc):
            if abs(sprite_loc - current_pixel) <= 1:
                self.pixels += '#'
            else:
                self.pixels += '.'
            if current_pixel == (self.width - 1):
                self.pixels += '\n'
            yield

    def run(self):
        while True:
            try:
                self.__next__()
            except StopIteration:
                break

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

def get_solution_2(data):
    screen = Screen(data)
    screen.run()
    return screen

if __name__ == "__main__":
    solution_data = get_data()
    print('solution 1:', get_solution_1(solution_data))
    print(f'solution 2:\n{get_solution_2(solution_data)}')
