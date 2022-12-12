import re
from collections import deque

def get_data():
    with open('input', 'r') as f:
        data = f.read()
    return data

def get_re():
    get_num = r'^Monkey\s(?P<number>[0-9]+):\n'
    get_items = r"^\s{2}Starting\sitems:\s(?P<items>[0-9, ]+)\n"
    get_op = r'^\s{2}Operation:\s(?P<operation>[0-9a-z*+= ]+)\n'
    get_test = r'^\s{2}Test:\s(?P<test>[a-z0-9 ]+)\n'
    get_true = r'^\s{4}If\strue:\sthrow\sto\smonkey\s(?P<if_true>[0-9]+)\n'
    get_false = r'\s{4}If\sfalse:\sthrow\sto\smonkey\s(?P<if_false>[a-z0-9 ]+)$'
    regex = fr'''(?xms)  # Sets MULTILINE, VERBOSE, and DOTALL flags
        {get_num}   # gets the monkey's number
        {get_items} # gets the monkey's starting items
        {get_op}    # gets the operation the monkey performs on the item
        {get_test}  # gets the test that determins where the monkey will throw
        {get_true}  # - where the monkey throws if the test is true
        {get_false} # - where the monkey throws if the test is false
        '''
    return regex

class Monkey:
    def __init__(self, num, relief=3):
        self.num = num
        self.relief = relief
        self.items = deque()
        self.true_monkey = None
        self.false_monkey = None
        self.factor = None
        self.monkey_around = None
        self.curiosity = 0

    # def __repr__(self):
    #     return f'< Monkey: {self.num} items: {self.items} >'

    def set_test_factor(self, test_str):
        match = re.match(r'divisible by (?P<num>[0-9]+)', test_str)
        self.factor = int(match.group('num'))

    def set_operation(self, op_str):
        op_str = op_str.replace('new =', 'lambda old:')
        self.monkey_around = eval(op_str)


    def inspect(self):
        # if not self.items:
        #     return
        while self.items:
            item = self.items.popleft()
            item = self.monkey_around(item) // self.relief
            self.throw(item)
            self.curiosity += 1

        # for item in self.items:
        #     monkeyed_item = self.monkey_around(item)
        #     monkeyed_item = monkeyed_item // self.relief
        #     self.throw(monkeyed_item)
        #     self.curiosity += 1
        # self.items = []

    def throw(self, item):
        if item % self.factor == 0:
            self.true_monkey.catch(item)
        else:
            self.false_monkey.catch(item)

    def catch(self, item):
        self.items.append(item)

class Barrel:
    def __init__(self, data, relief=3):
        self.data = data
        self.regex = get_re()
        self.monkeys = []
        self.get_monkeys(relief)

    def get_monkeys(self, relief):
        monkey_dicts = [i.groupdict()
                        for i in re.finditer(self.regex, self.data)]
        self.monkeys = [Monkey(v, relief)
                        for v, monkey in enumerate(monkey_dicts)]
        for monkey, monkey_dict in zip(self.monkeys, monkey_dicts):
            monkey.items = deque([int(i) for i in monkey_dict['items'].split(', ')])
            true_monkey = self.monkeys[int(monkey_dict['if_true'])]
            false_monkey = self.monkeys[int(monkey_dict['if_false'])]
            monkey.true_monkey = true_monkey
            monkey.false_monkey = false_monkey
            monkey.set_operation(monkey_dict['operation'])
            monkey.set_test_factor(monkey_dict['test'])

    def monkey_a_round(self, rounds=1):
        for i in range(rounds):
            for monkey in self.monkeys:
                monkey.inspect()

    def monkey_business(self):
        curious_monkeys = sorted([monkey.curiosity for monkey in self.monkeys])
        return curious_monkeys[-2] * curious_monkeys[-1]

def get_solution_1(data):
    barrel = Barrel(data)
    barrel.monkey_a_round(20)
    return barrel.monkey_business()

def get_solution_2(data):
    return data[:10]

if __name__ == "__main__":
    solution_data = get_data()
    solution_1 = get_solution_1(solution_data)
    print("Solution 1:", solution_1)
    solution_2 = get_solution_2(solution_data)
    print("Solution 2:", solution_2)
