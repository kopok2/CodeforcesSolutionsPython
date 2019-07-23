class CodeforcesTask22ASolution:
    def __init__(self):
        self.result = ''
        self.sequence = []

    def read_input(self):
        input()
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.sequence.sort()
        m = self.sequence[0]
        r = "NO"
        for x in self.sequence:
            if x > m:
                r = x
                break
        self.result = str(r)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask22ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
