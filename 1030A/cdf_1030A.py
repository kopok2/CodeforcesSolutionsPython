class CodeforcesTask1030ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.response = []

    def read_input(self):
        self.n = int(input())
        self.response = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.result = "easy" if 1 not in self.response else "hard"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1030ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
