class CodeforcesTask641ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.directions = []
        self.jump_lengths = []

    def read_input(self):
        self.n = int(input())
        self.directions = input()
        self.jump_lengths = [int(x) for x in input().split(" ")]

    def process_task(self):
        jumps = 0
        pos = 1
        out = False
        while jumps < self.n * 10 and not out:
            jumps += 1
            pos += (-1 if self.directions[pos - 1] == "<" else 1) * self.jump_lengths[pos - 1]
            if pos < 1 or pos > self.n:
                out = True
        self.result = "FINITE" if out else "INFINITE"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask641ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
