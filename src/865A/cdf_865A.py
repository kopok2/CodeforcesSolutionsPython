class CodeforcesTask865ASolution:
    def __init__(self):
        self.result = ''
        self.a = 0

    def read_input(self):
        self.a = int(input())

    def process_task(self):
        n = self.a * 2 - 1
        m = 2
        coins = [1, 2]
        self.result = "{0} {1}\n{2}".format(n, m, " ".join([str(x) for x in coins]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask865ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
