class CodeforcesTask282ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.instructions = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.instructions.append(input())

    def process_task(self):
        x = 0
        for instr in self.instructions:
            if "-" in instr:
                x -= 1
            else:
                x += 1
        self.result = str(x)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask282ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
