class CodeforcesTask421ASolution:
    def __init__(self):
        self.result = ''
        self.n_a_b = []
        self.a = []
        self.b = []

    def read_input(self):
        self.n_a_b = [int(x) for x in input().split(" ")]
        self.a = [int(x) for x in input().split(" ")]
        self.b = [int(x) for x in input().split(" ")]

    def process_task(self):
        resulting = [1 if x + 1 in self.a else 2 for x in range(self.n_a_b[0])]
        self.result = " ".join([str(x) for x in resulting])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask421ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
