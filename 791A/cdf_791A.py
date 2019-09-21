class CodeforcesTask791ASolution:
    def __init__(self):
        self.result = ''
        self.a_b = []

    def read_input(self):
        self.a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        y = 0
        while self.a_b[0] <= self.a_b[1]:
            y += 1
            self.a_b[0] *= 3
            self.a_b[1] *= 2
        self.result = str(y)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask791ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
