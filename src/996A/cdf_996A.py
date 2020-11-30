class CodeforcesTask996ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        coins = [100, 20, 10, 5, 1]
        used = 0
        while self.n:
            coin = coins.pop(0)
            used += self.n // coin
            self.n = self.n % coin
        self.result = str(used)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask996ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
