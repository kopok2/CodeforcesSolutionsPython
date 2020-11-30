class CodeforcesTask424ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.state = ''

    def read_input(self):
        self.n = int(input())
        self.state = input()

    def process_task(self):
        to = self.n // 2 - min(self.state.count('x'), self.state.count("X"))
        a = "x" if self.state.count('x') < self.state.count("X") else "X"
        b = "x" if self.state.count('x') > self.state.count("X") else "X"
        x = to
        while x:
            x -= 1
            self.state = self.state.replace(b, a, 1)
        self.result = str(to) + "\n" + self.state

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask424ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
