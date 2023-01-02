class Zero:
    def __init__(self, lst):
        self.lst = lst
        self.zero_history = []

    def zero_sum(self):
        for i in self.lst:
            for j in self.lst:
                for k in self.lst:
                    if i + j + k == 0:
                        self.zero_history.append([i, j, k])
                        self.lst.remove(i)
                        self.lst.remove(j)
                        self.lst.remove(k)
        return self.zero_history


obj = Zero([5, 7, -12, 6, 5, 7, 9, -7, 4, 3])
print(obj.zero_sum())