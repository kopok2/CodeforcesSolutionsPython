class CodeforcesTask454ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0

    def read_input(self):
        self.n = int(input())

    def process_task(self):
        g = self.n // 2
        p = -1
        x = 0
        result = []
        while x < self.n:
            result.append("*" * g + "D" * (self.n - 2 * g) + "*" * g)
            g += p
            if not g:
                p = -p
            x += 1
        self.result = "\n".join(result)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask454ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
