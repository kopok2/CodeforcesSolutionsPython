class CodeforcesTask732ASolution:
    def __init__(self):
        self.result = ''
        self.k_r = []

    def read_input(self):
        self.k_r = [int(x) for x in input().split(" ")]

    def process_task(self):
        for k in range(1, 10):
            price = self.k_r[0] * k
            if not (price - self.k_r[1]) % 10:
                self.result = str(k)
                break
            if not price % 10:
                self.result = str(k)
                break

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask732ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
