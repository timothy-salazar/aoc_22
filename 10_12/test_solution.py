from solution import ElfVM, Screen, get_signal_strength
from functools import cache

test_data_1 = [
    'noop',
    'addx 3',
    'addx -5',
]
@cache
def get_test_data_2():
    with open('test_input.txt', 'r') as f:
        data = f.read().strip().split('\n')
    return data

test_data_3 = '''##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
'''

###############
# Part 1 Tests:
###############
def test_vm_basic():
    vm = ElfVM(test_data_1)
    assert [i for i in vm] == [1, 1, 1, 4, 4, -1]

def test_vm_larger_program():
    data = get_test_data_2()
    vm = ElfVM(data)
    l = [i for i in vm]
    assert l[19] == 21
    assert l[59] == 19
    assert l[99] == 18
    assert l[139] == 21
    assert l[179] == 16
    assert l[219] == 18

def test_vm_signal_strength():
    data = get_test_data_2()
    vm = ElfVM(data)
    l = [i*(v+1) for v, i in enumerate(vm)]
    assert l[slice(19, 220, 40)] == [420, 1140, 1800, 2940, 2880, 3960]

def test_get_signal_strength():
    data = get_test_data_2()
    vm = ElfVM(data)
    assert get_signal_strength(vm, 19, 220, 40) == 13140

################
# Part 2 Tests:
################
def test_screen_basic():
    data = get_test_data_2()
    screen = Screen(data)
    assert screen.pixels == ''
    expected_row = '##..##..##..##..##..#'
    for i in range(1, len(expected_row)):
        screen.__next__()
        assert screen.pixels == expected_row[:i]

def test_screen_full():
    data = get_test_data_2()
    screen = Screen(data)
    screen.run()
    assert screen.pixels == test_data_3
