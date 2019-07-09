class CodeforcesTask139ASolution:
    def __init__(self):
        self.result = ''
        self.pages = 0
        self.schedule =[]

    def read_input(self):
        self.pages = int(input())
        self.schedule = [int(x) for x in input().split(" ")]

    def process_task(self):
        dayweek = 1
        while self.pages > 0:
            self.pages -= self.schedule[dayweek - 1]

            dayweek += 1
            if dayweek > 7:
                dayweek = 1
        if dayweek > 1:
            self.result = str(dayweek - 1)
        else:
            self.result = "7"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask139ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
