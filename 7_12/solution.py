TOTAL_DISK_SPACE = 70000000
NEEDED_SPACE = 30000000

class Directory:

    def __init__(self, f, name='/', parent=None):
        self.name = name
        self.parent = parent
        self.children = dict()
        self.files = dict()
        self.file_sizes = 0
        self.f = f

    def __repr__(self):
        return f'< Directory: {self.name} >'

    def process_lines(self):
        line = self.f.readline()
        if not line:
            return
        self.input(line)

    def input(self, line):
        if line[0] == '$':
            self.command(line)
        else:
            self.add_contents(line)

    def command(self, line):
        parts = line.split()
        if parts[1] == 'ls':
            self.process_lines()
        elif parts[1] == 'cd':
            self.enter_dir(parts[2])

    def add_contents(self, line):
        while line and (line[0] != '$'):
            properties, name = line.split()
            if properties == 'dir':
                if self.name == '/':
                    dir_name = '/' + name
                else: 
                    dir_name = self.name+'/'+name
                self.children[name] = Directory(
                    self.f,
                    dir_name,
                    self)
            else:
                self.file_sizes += int(properties)
                self.files[name] = int(properties)
            line = self.f.readline()
        if line:
            self.input(line)

    def enter_dir(self, dir_name):
        if dir_name == '..':
            self.parent.process_lines()
        elif dir_name == '/':
            if self.name == '/':
                self.process_lines()
            else:
                self.parent.enter_dir(dir_name)
        else:
            self.children[dir_name].process_lines()

    def size(self):
        dir_sizes = sum([child.size() for child in self.children.values()])
        return self.file_sizes + dir_sizes
    
    def all_dirs(self):
        dir_list = []
        if self.name == '/':
            dir_list.append(self)
        if self.children:
            dir_list += [child for child in self.children.values()]
            for child in self.children.values():
                dir_list += child.all_dirs()
        else:
            return []
        return dir_list
    
    def free_space(self):
        return TOTAL_DISK_SPACE - self.size 

def get_solution_1(d):
    size_list = [i.size() for i in d.all_dirs()]
    return sum([i for i in size_list if i <= 100000])

def get_solution_2(d):
    size_list = sorted([i.size() for i in d.all_dirs()])
    for size in size_list:
        if (size + d.free_space()) >= NEEDED_SPACE:
            return size

if __name__ == "__main__":
    with open('input', 'r') as file_handle:
        root_dir = Directory(file_handle)
        root_dir.process_lines()
    solution_1 = get_solution_1(root_dir)
    print('solution 1:', solution_1)
    solution_2 = get_solution_2(root_dir)
    print('solution 2:', solution_2)