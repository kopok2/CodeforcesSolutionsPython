class CodeforcesTask560ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.notes = []

    def read_input(self):
        self.n = int(input())
        self.notes = [int(x) for x in input().split(" ")]

    def process_task(self):
        if 1 in self.notes:
            self.result = "-1"
        else:
            self.result = "1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask560ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
