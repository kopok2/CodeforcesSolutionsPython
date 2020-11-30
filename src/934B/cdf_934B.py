class CodeforcesTask934BSolution:
    def __init__(self):
        self.result = ''
        self.k = 0

    def read_input(self):
        self.k = int(input())

    def process_task(self):
        if self.k > 36:
            res = -1
        else:
            res = []
            while self.k:
                if self.k >= 2:
                    res.append(8)
                    self.k -= 2
                else:
                    res.append(4)
                    self.k -= 1
            res = int("".join([str(x) for x in res]))
        self.result = str(res)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask934BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
