class CodeforcesTask350ASolution:
    def __init__(self):
        self.result = ''
        self.correct_times = []
        self.wrong_times = []

    def read_input(self):
        input()
        self.correct_times = [int(x) for x in input().split(" ")]
        self.wrong_times = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.correct_times.sort()
        self.wrong_times.sort()
        if self.correct_times[0] * 2 < self.correct_times[-1]:
            solution = self.correct_times[-1]
        else:
            solution = self.correct_times[0] * 2
        if not solution < self.wrong_times[0]:
            solution = -1
        self.result = str(solution)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask350ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
