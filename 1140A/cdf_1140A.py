class CodeforcesTask1140ASolution:
    def __init__(self):
        self.result = ''
        self.pages = 0
        self.mysteries = []

    def read_input(self):
        self.pages = int(input())
        self.mysteries = [int(x) for x in input().split(" ")]

    def process_task(self):
        days = 0
        page = 1
        mystery = self.mysteries[0]
        while page <= self.pages:

            if self.mysteries[page - 1] > mystery:
                mystery = self.mysteries[page - 1]
            if mystery == page:
                days += 1
            page += 1
        self.result = str(days)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1140ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
