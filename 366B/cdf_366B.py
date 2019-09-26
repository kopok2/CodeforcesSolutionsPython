class CodeforcesTask366BSolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.tells = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.tells = [int(x) for x in input().split(" ")]

    def process_task(self):
        telling = [0] * self.n_k[1]
        for x in range(self.n_k[0]):
            telling[x % self.n_k[1]] += self.tells[x]
        self.result = str(telling.index(min(telling)) + 1)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask366BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
