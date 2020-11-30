class CodeforcesTask897ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.string = []
        self.operations = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.string = list(input())
        for x in range(self.n_m[1]):
            self.operations.append(input().split(" "))

    def process_task(self):
        for op in self.operations:
            for x in range(int(op[0]) - 1, int(op[1])):
                if self.string[x] == op[2]:
                    self.string[x] = op[3]
        self.result = "".join(self.string)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask897ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
