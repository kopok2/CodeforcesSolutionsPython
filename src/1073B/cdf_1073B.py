class CodeforcesTask1073BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.books = []
        self.order = []

    def read_input(self):
        self.n = int(input())
        self.books = [int(x) for x in input().split(" ")]
        self.order = [int(x) for x in input().split(" ")]

    def process_task(self):
        res = []
        used = {}
        self.order = self.order[::-1]
        self.books = self.books[::-1]
        while self.order:
            cc = 0
            taking = self.order.pop(-1)
            if taking not in used:
                d = self.books.pop(-1)
                used[d] = True
                cc = 1
                while d != taking:
                    d = self.books.pop(-1)
                    cc += 1
                    used[d] = True
            res.append(cc)
        self.result = ' '.join([str(x) for x in res])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1073BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
