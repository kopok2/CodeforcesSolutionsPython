class CodeforcesTask999ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.problems = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]
        self.problems = [int(x) for x in input().split(" ")]

    def process_task(self):
        left = 0
        right = 0
        for x in range(len(self.problems)):
            if self.n_k[1] >= self.problems[x]:
                left += 1
            else:
                break
        for x in range(len(self.problems)):
            if self.n_k[1] >= self.problems[len(self.problems) - x - 1]:
                right += 1
            else:
                break
        if left + right > len(self.problems):
            result = len(self.problems)
        else:
            result = left + right
        self.result = str(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask999ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
