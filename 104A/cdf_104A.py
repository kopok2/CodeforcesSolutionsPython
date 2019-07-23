class CodeforcesTask104ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        deck = [[x, x, x, x] for x in range(1, 12)]
        deck.append([10 for x in range(11)])
        mdeck = []
        for d in deck:
            mdeck += d
        self.result = str(mdeck.count(self.n - 10))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask104ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
