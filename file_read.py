from enum import Enum




# store seperate lists as dictionary entries
class Parser(object):

# define allowable states for Parser
    class State(Enum):
        head = 1
        value = 2
        blank = 3

# inital instance of Parser
    def __init__(self):
        self.categories = {}
        self.current_header = None

# define states
    def line_state(self, line):
        if '`' in line:
            return Parser.State.blank
        elif '*' in line:
            return Parser.State.head
        elif len(line) > 2:
            return Parser.State.value

# specify state handling
    def line_handle(self, state, line):
        if state is Parser.State.head:
            self.current_header = line.replace('*','')
            self.categories[self.current_header]=[]
        elif state is Parser.State.value:
            current_values = self.categories[self.current_header]
            current_values.append(line)

# combine file read, clean, state, and handling
    def run(self, edit_file):
        with open(edit_file) as src:
            for l in src.readlines():
                c = l.rstrip(',\n ')
                s = self.line_state(c)
                self.line_handle(s,c)
        return self.categories
