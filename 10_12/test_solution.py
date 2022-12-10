from solution import ElfVM

test_data_1 = [
    'noop',
    'addx 3',
    'addx -5',
]

def test_vm():
    vm = ElfVM(test_data_1)
    assert [i for i in vm] == [1,1,1,4,4,-1]
    # assert vm.register == 1
    # assert vm.__next__() == 1
    # assert vm.__next__() == 1
    # assert vm.__next__() == 4
    # assert vm.__next__() == 4
    # assert vm.__next__() == -1

