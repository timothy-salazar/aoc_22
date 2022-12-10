from solution import ElfVM, get_signal_strength

test_data_1 = [
    'noop',
    'addx 3',
    'addx -5',
]

def test_vm_basic():
    vm = ElfVM(test_data_1)
    assert [i for i in vm] == [1, 1, 1, 4, 4, -1]

def test_vm_larger_program():
    with open('test_input.txt', 'r') as f:
        data = f.read().strip().split('\n')
    vm = ElfVM(data)
    l = [i for i in vm]
    assert l[19] == 21
    assert l[59] == 19
    assert l[99] == 18
    assert l[139] == 21
    assert l[179] == 16
    assert l[219] == 18

def test_vm_signal_strength():
    with open('test_input.txt', 'r') as f:
        data = f.read().strip().split('\n')
    vm = ElfVM(data)
    l = [i*(v+1) for v, i in enumerate(vm)]
    assert l[slice(19, 220, 40)] == [420, 1140, 1800, 2940, 2880, 3960]

def test_get_signal_strength():
    with open('test_input.txt', 'r') as f:
        data = f.read().strip().split('\n')
    vm = ElfVM(data)
    assert get_signal_strength(vm, 19, 220, 40) == 13140