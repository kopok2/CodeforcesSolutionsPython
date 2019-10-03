class CodeforcesTask1220ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.cards = []

    def read_input(self):
        self.n = int(input())
        self.cards = input()

    def process_task(self):
        ones = self.cards.count("n")
        zeros = self.cards.count("z")
        self.result = " ".join([str(x) for x in [1] * ones + [0] * zeros])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1220ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
