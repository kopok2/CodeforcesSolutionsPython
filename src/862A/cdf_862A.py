def mex(s):
    for x in range(102):
        if x not in s:
            return x


class CodeforcesTask862ASolution:
    def __init__(self):
        self.result = ''
        self.n_x = []
        self.set = []

    def read_input(self):
        self.n_x = [int(x) for x in input().split(" ")]
        self.set = [int(x) for x in input().split(" ")]

    def process_task(self):
        operations = 0
        while mex(self.set) != self.n_x[1]:
            operations += 1
            if mex(self.set) > self.n_x[1]:
                self.set.remove(self.n_x[1])
            else:
                self.set.append(mex(self.set))
        self.result = str(operations)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask862ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
