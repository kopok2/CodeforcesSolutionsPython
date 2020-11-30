class CodeforcesTask546ASolution:
    def __init__(self):
        self.result = ''
        self.k_n_w = []

    def read_input(self):
        self.k_n_w = [int(x) for x in input().split(" ")]

    def process_task(self):
        all_price = 0
        for x in range(self.k_n_w[2]):
            all_price += self.k_n_w[0] * (x + 1)
        missing = -(self.k_n_w[1] - all_price)
        self.result = str(max(0, missing))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask546ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
