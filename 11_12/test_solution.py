import re
from solution import get_re, Monkey, Barrel
from monkey_list import monkey_list, round_results

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
    barrel = Barrel(data)

      