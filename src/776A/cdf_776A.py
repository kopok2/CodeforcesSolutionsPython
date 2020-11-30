class CodeforcesTask776ASolution:
    def __init__(self):
        self.result = ''
        self.pair = []
        self.n = 0
        self.murder_replace = []

    def read_input(self):
        self.pair = input().split(" ")
        self.n = int(input())
        for _ in range(self.n):
            self.murder_replace.append(input().split(" "))

    def process_task(self):
        res = []
        to_choose = set(self.pair)
        for day in self.murder_replace:
            res.append(" ".join(to_choose))
            to_choose.remove(day[0])
            to_choose.add(day[1])
        res.append(" ".join(to_choose))
        self.result = "\n".join(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask776ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
