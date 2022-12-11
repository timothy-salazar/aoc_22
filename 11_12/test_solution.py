import re
from solution import get_re
from monkey_list import monkey_list

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
            
