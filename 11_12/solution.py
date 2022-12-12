import re

def get_data():
    with open('input', 'r') as f:
        data = f.read()
    return data

def get_re():
    get_num = r'^Monkey\s(?P<number>[0-9]+):\n'
    get_items = r"^\s{2}Starting\sitems:\s(?P<items>[0-9, ]+)\n"
    get_op = r'^\s{2}Operation:\s(?P<operation>[0-9a-z*+= ]+)\n'
    get_test = r'^\s{2}Test:\sdivisible\sby\s(?P<test>[0-9 ]+)\n'
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

class Item:
    def __init__(self, val, factors):
        self.val = int(val)
        self.factors = factors
        self.fdict = {i:val%i for i in self.factors}

    def __add__(self, num):
        for f in self.factors:
            self.fdict[f] = (self.fdict[f] + num) % f
        return self

    def __mul__(self, num):
        for f in self.factors:
            self.fdict[f] = (self.fdict[f] * num) % f
        return self

    def __pow__(self, num, x=None):
        for f in self.factors:
            self.fdict[f] = (self.fdict[f]**num) % f
        return self
    
    def __mod__(self, num):
        return self.fdict[num]
    
    def __floordiv__(self, num):
        return self

class Monkey:
    def __init__(self, num, monkey_dict, relief=3):
        self.num = num
        self.relief = relief
        self.curiosity = 0
        self.items = []
        self.true_monkey = None
        self.false_monkey = None

        # Operation variables
        self.factor = int(monkey_dict['test'])
        self.add = 0
        self.mult = 1
        self.exp = 1
        self.set_operation(monkey_dict['operation'])


    def set_operation(self, op_str):
        op_re = r'new = old [+*] (?P<other>[0-9old]+)'
        match = re.match(op_re, op_str)
        if not match:
            raise ValueError('got weird operation string')
        other = match.group('other')
        if '+' in op_str:
            if other == 'old':
                self.mult = 2
            else:
                self.add = int(other)
        elif '*' in op_str:
            if other == 'old':
                self.exp = 2
            else:
                self.mult = int(other)
        # op_str = op_str.replace('new =', 'lambda old:')
        # self.monkey_around = eval(op_str)

    def monkey_around(self, item):
        item = item + self.add
        item = item * self.mult
        item = item ** self.exp
        item = item // self.relief
        return item


    def inspect(self):
        for item in self.items:
            item = self.monkey_around(item)
            self.throw(item)
            self.curiosity += 1
        self.items = []

    def throw(self, item):
        if item % self.factor == 0:
            self.true_monkey.catch(item)
        else:
            self.false_monkey.catch(item)

    def catch(self, item):
        self.items.append(item)

class Barrel:
    def __init__(self, data, relief=3, king_kong_mode=False):
        self.data = data
        self.regex = get_re()
        self.monkeys = []
        self.rounds = 0
        self.get_monkeys(relief, king_kong_mode)

    def get_monkeys(self, relief, king_kong_mode):
        monkey_dicts = [i.groupdict()
                        for i in re.finditer(self.regex, self.data)]
        self.monkeys = [Monkey(v, monkey_dict, relief)
                        for v, monkey_dict in enumerate(monkey_dicts)]
        factor_list = [monkey.factor for monkey in self.monkeys]
        for monkey, monkey_dict in zip(self.monkeys, monkey_dicts):
            items = [int(i) for i in monkey_dict['items'].split(', ')]
            if king_kong_mode:
                monkey.items = [Item(i, factor_list) for i in items]
            else:
                monkey.items = [i for i in items]
            true_monkey = self.monkeys[int(monkey_dict['if_true'])]
            false_monkey = self.monkeys[int(monkey_dict['if_false'])]
            monkey.true_monkey = true_monkey
            monkey.false_monkey = false_monkey

    def monkey_a_round(self, rounds=1):
        for i in range(rounds):
            self.rounds += 1
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
    barrel = Barrel(data, relief=1, king_kong_mode=True)
    barrel.monkey_a_round(10000)
    return barrel.monkey_business()

if __name__ == "__main__":
    solution_data = get_data()
    solution_1 = get_solution_1(solution_data)
    print("Solution 1:", solution_1)
    solution_2 = get_solution_2(solution_data)
    print("Solution 2:", solution_2)
