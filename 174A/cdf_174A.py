class CodeforcesTask174ASolution:
    def __init__(self):
        self.result = ''
        self.n_b = []
        self.capacity = []

    def read_input(self):
        self.n_b = [int(x) for x in input().split(" ")]
        self.capacity = [int(x) for x in input().split(" ")]

    def process_task(self):
        mx = max(self.capacity)
        to_fill = sum([mx - x for x in self.capacity])
        if to_fill > self.n_b[1]:
            self.result = "-1"
        else:
            result = []
            for x in self.capacity:
                result.append(mx - x + (self.n_b[1] - to_fill) / self.n_b[0])
            self.result = "\n".join([str(y) for y in result])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask174ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
