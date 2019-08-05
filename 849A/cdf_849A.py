class CodeforcesTask849ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.sequence = []

    def read_input(self):
        self.n = int(input())
        self.sequence = [int(x) for x in input().split(" ")]

    def process_task(self):
        if not self.n % 2:
            self.result = "No"
        elif self.sequence[0] % 2 == 0:
            self.result = "No"
        elif self.sequence[-1] % 2 == 0:
            self.result = "No"
        else:
            self.result = "Yes"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask849ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
