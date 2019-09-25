class CodeforcesTask268BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        cost = self.n
        base_cost = 1
        unknown = self.n
        for layer in range(1, self.n):
            cost += base_cost * (unknown - 1)
            base_cost += 1
            unknown -= 1
        self.result = str(cost)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask268BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
