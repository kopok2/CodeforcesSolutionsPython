class CodeforcesTask339BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.tasks = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        self.tasks = [int(x) for x in input().split(" ")]

    def process_task(self):
        time_needed = 0
        position = 1
        for task in self.tasks:
            if task > position:
                time_needed += task - position
                position = task
            elif task < position:
                time_needed += task + self.n_m[0] - position
                position = task
        self.result = str(time_needed)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask339BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
