class CodeforcesTask733BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.columns = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.columns.append([int(y) for y in input().split(" ")])

    def process_task(self):
        left = sum([x[0] for x in self.columns])
        right = sum([x[1] for x in self.columns])
        tb_basic = abs(left - right)
        mx_b = tb_basic
        chosen = 0
        for x in range(self.n):
            nl = left - self.columns[x][0]
            nr = right - self.columns[x][1]
            nb = abs(nl + self.columns[x][1] - nr - self.columns[x][0])
            if mx_b < nb:
                chosen = x + 1
                mx_b = nb
        self.result = str(chosen)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask733BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
