class CodeforcesTask869BSolution:
    def __init__(self):
        self.result = ''
        self.a_b = []

    def read_input(self):
        self.a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.a_b[1] - self.a_b[0] < 10:
            result = 1
            for x in range(self.a_b[0] + 1, self.a_b[1] + 1):
                result *= x
            self.result = str(result)[-1]
        else:
            result = 1
            for x in range(self.a_b[1] - 9, self.a_b[1] + 1):
                result *= x
            self.result = str(result)[-1]

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask869BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
