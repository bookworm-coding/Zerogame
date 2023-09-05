from pandas import DataFrame


class Zero(DataFrame):
    n = 0
    l = []

    def __init__(self, n: int):
        self.n = n
        for i in range(2 * self.n + 1):
            self.l.append([])
        self.zero([])
        super().__init__(data=self.dataframe())

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


if __name__ == "__main__":
    number = int(input("제로게임 인원수를 입력하세요: "))
    select = input("엑셀 파일을 원하면 E를, 텍스트 파일을 원하면 T를, 단순 출력을 원하면 P를 입력하세요")
    if select == "E":
        Zero(number).to_excel("result.xlsx")
    elif select == "T":
        f = open("result.txt", "w")
        print(Zero(number), file=f)
    elif select == "P":
        print(Zero(number))
    else:
        print("잘못된 입력입니다. 다시 실행해주세요.")
