import sys


class Indenter:

    def __init__(self):
        self.indent_level = -1

    def __enter__(self):
        self.indent_level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.indent_level -= 1

    def print(self, string):
        tab = '\t'
        sys.stdout.write(f'{tab * self.indent_level}{string}\n')


with Indenter() as indent:
    indent.print("Hi")
    with indent:
        indent.print("Talk is Cheap!")
        with indent:
            indent.print("Show me the Code...")
    indent.print("Torvalds")
