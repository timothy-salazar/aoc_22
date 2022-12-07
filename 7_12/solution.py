import re

class Directory:

    def __init__(self, f, name='/', parent=None):
        self.name = name
        self.parent = parent
        self.children = dict()
        self.files = dict()
        self.f = f
        #self.process_lines()

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
                #self.children.append(Directory(name, self, self.f))
                self.children[name] = Directory(self.f, name, self)
            else:
                self.files[name] = int(properties)
            line = self.f.readline()

        
        # line = self.f.readline()

        ## this seemed to work, but changing for reasons 
        # properties, name = line.split()
        # if properties == 'dir':
        #     self.children[name] = Directory(self.f, name, self)
        # else:
        #     self.files[name] = int(properties)
        # self.process_lines()

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


# class Thing:
#     def __init__(self, f, parent=None):
#         self.f = f
#         self.parent = parent
#         self.thing()
    
#     def thing(self):
#         print(self.f.readline())
#         if self.parent:
#             return
#         else:
#             thing = Thing(self.f, self)