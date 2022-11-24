import termcolor


class Table:
    def __init__(self):
        self.table_map = dict().fromkeys(range(1, 10), '')
        # print(self.table_map)

    def table(self):
        print("""
|\t{}\t|\t{}\t|\t{}\t|        
|\t{}\t|\t{}\t|\t{}\t|        
|\t{}\t|\t{}\t|\t{}\t|        
        """.format(*self.table_map.values()))

    def set(self, cell, sign):
        if not self.table_map.get(cell):
            self.table_map[cell] = sign
        else:
            print(termcolor.colored(f'position "{cell}" currently set. ', 'red'))\



