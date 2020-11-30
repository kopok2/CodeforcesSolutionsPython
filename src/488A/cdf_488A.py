class CodeforcesTask488ASolution:
    def __init__(self):
        self.result = ''
        self.a = 0

    def read_input(self):
        self.a = int(input())

    def process_task(self):
        steps = 1
        while not "8" in str(self.a + steps):
            steps += 1
        self.result = str(steps)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask488ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
