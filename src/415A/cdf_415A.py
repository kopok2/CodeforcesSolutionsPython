class CodeforcesTask415ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.buttons = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.buttons = [int(x) for x in input().split(" ")]

    def process_task(self):
        off_by = [0 for x in range(self.n_m[0])]
        for button in self.buttons:
            for y in range(button - 1, self.n_m[0]):
                if not off_by[y]:
                    off_by[y] = button
        self.result = " ".join([str(x) for x in off_by])

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask415ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
