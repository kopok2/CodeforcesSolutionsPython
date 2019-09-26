class CodeforcesTask719ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.moon = []

    def read_input(self):
        self.n = int(input())
        self.moon = [int(x) for x in input().split(" ")]

    def process_task(self):
        if self.moon[-1] == 0:
            self.result = "UP"
        elif self.moon[-1] == 15:
            self.result = "DOWN"
        elif self.n == 1:
            self.result = "-1"
        elif self.moon[-1] > self.moon[-2]:
            self.result = "UP"
        else:
            self.result = "DOWN"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask719ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
