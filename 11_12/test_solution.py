import re
from solution import get_re, Barrel, Monkey
from monkey_list import monkey_list, round_results, round_results_part_2
from datetime import datetime

def get_test_data():
    with open('test_input.txt', 'r') as f:
        data = f.read()
    return data

class TestRE:
    regex = get_re()
    data = get_test_data()

    def test_one(self):
        monkey_0 = '\n'.join(self.data.split('\n')[:6])
        match = re.match(self.regex, monkey_0)
        expected = monkey_list[0]
        assert match.groupdict() == expected

    def test_all(self):
        matches = [i for i in re.finditer(self.regex, self.data)]
        for expected, match in zip(monkey_list, matches):
            assert expected == match.groupdict()

class TestBarrelOfMonkeys:
    data = get_test_data()
    barrel = Barrel(data)

    def test_basic(self):
        monkey = self.barrel.monkeys[0]
        assert monkey.num == 0
        assert monkey.items == [79, 98]
        assert monkey.factor == 23
        assert monkey.true_monkey is self.barrel.monkeys[2]
        assert monkey.false_monkey is self.barrel.monkeys[3]
    
    def test_inspect(self):
        monkey = self.barrel.monkeys[0]
        destination_monkey = self.barrel.monkeys[3]
        monkey.inspect()
        assert monkey.num == 0
        assert monkey.items == []
        assert monkey.factor == 23
        assert destination_monkey.items == [74, 500, 620]
        
    def test_round_1(self):
        self.barrel = Barrel(self.data)
        self.barrel.monkey_a_round()
        assert self.barrel.monkeys[0].items == [20, 23, 27, 26]
        assert self.barrel.monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
        assert self.barrel.monkeys[2].items == []
        assert self.barrel.monkeys[3].items == []

    def test_round_2(self):
        self.barrel = Barrel(self.data)
        for i in range(1, 21):
            self.barrel.monkey_a_round()
            if i not in round_results:
                continue
            for expected, monkey in zip(round_results[i], self.barrel.monkeys):
                assert monkey.items == expected

    def test_curiosity(self):
        self.barrel = Barrel(self.data)
        self.barrel.monkey_a_round(20)
        assert self.barrel.monkeys[0].curiosity == 101
        assert self.barrel.monkeys[1].curiosity == 95
        assert self.barrel.monkeys[2].curiosity == 7
        assert self.barrel.monkeys[3].curiosity == 105

class TestBarrelPt2:
    data = get_test_data()
    barrel = Barrel(data, relief=1, king_kong_mode=True)

    def test_serious_monkey_business(self):
        now = datetime.now()
        last_round = 0
        for round_info in round_results_part_2:
            this_round = round_info['round']
            self.barrel.monkey_a_round(this_round - last_round)
            for v, monkey in enumerate(self.barrel.monkeys):
                assert monkey.curiosity == round_info[f'monkey_{v}']
            last_round = this_round
        time_elapsed = datetime.now() - now
        print(f'{time_elapsed.seconds//60} minutes {time_elapsed.seconds%60} seconds')

    def test_final_monkey_business(self):
        curiosity = sorted([monkey.curiosity for monkey in self.barrel.monkeys])
        assert curiosity[-2:] == [52013, 52166]
        assert self.barrel.monkey_business() == 2713310158

# def thing(relief=1):
#     regex = get_re()
#     data = get_test_data()
#     monkeys = []
#     monkey_dicts = [i.groupdict()
#                         for i in re.finditer(regex, data)]
#     monkeys = [Monkey(v, relief) 
#                     for v, monkey in enumerate(monkey_dicts)]
#     for monkey, monkey_dict in zip(monkeys, monkey_dicts):
#         monkey.items = [int(i) for i in monkey_dict['items'].split(', ')]
#         true_monkey = monkeys[int(monkey_dict['if_true'])]
#         false_monkey = monkeys[int(monkey_dict['if_false'])]
#         monkey.true_monkey = true_monkey
#         monkey.false_monkey = false_monkey
#         monkey.set_operation(monkey_dict['operation'])
#         monkey.set_test_factor(monkey_dict['test'])
#     return monkeys

# if __name__ == "__main__":
#     tb = TestBarrelPt2()
#     tb.test_serious_monkey_business()