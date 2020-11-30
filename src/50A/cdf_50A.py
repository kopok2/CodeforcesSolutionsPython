class CodeforcesTask50ASolution:
    def __init__(self):
        self.result = ''
        self.size = []

    def read_input(self):
        self.size = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.result = str((self.size[0] * self.size[1]) // 2)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask50ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
