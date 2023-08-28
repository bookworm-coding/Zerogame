from pandas import DataFrame


class Zero(DataFrame):
    n = 0
    l = []

    def __init__(self, n: int):
        self.n = n
        for i in range(2 * self.n + 1):
            self.l.append([])
        self.zero([])
        super().__init__(data=self.dataframe(), columns=["맞는 경우들"])

    def __str__(self):
        s = ""
        for i in range(len(self.l)):
            s += str(i) + " : "
            for j in self.l[i]:
                s += str(j) + " "
            s += "\n"
        return s

    __repr__ = __str__

    def zero(self, a: list):
        if len(a) == self.n:
            s = 0
            for i in a:
                s += i
            self.l[s].append(tuple(a))
        else:
            self.zero(a + [0])
            self.zero(a + [1])
            self.zero(a + [2])

    def dataframe(self):
        l2 = []
        for i in self.l:
            s = ""
            for j in i:
                s += str(j) + " "
            l2.append(s)
        return l2

    def result(self):
        return self.l
