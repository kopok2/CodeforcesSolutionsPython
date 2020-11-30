class CodeforcesTask758ASolution:
    def __init__(self):
        self.result = ''
        self.welfare = []

    def read_input(self):
        input()
        self.welfare = [int(x) for x in input().split(" ")]

    def process_task(self):
        target = max(self.welfare)
        self.result = str(sum([target - x for x in self.welfare]))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask758ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
