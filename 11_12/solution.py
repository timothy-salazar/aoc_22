import re

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
    def __init__(self):
        pass

def get_solution_1(data):
    return ''

def get_solution_2(data):
    return ''

if __name__ == "__main__":
    solution_data = get_data()
    solution_1 = get_solution_1(solution_data)
    print("Solution 1:", solution_1)
    solution_2 = get_solution_2(solution_data)
    print("Solution 2:", solution_2)
