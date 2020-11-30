class CodeforcesTask112ASolution:
    def __init__(self):
        self.result = ''
        self.first = ''
        self.second = ''

    def read_input(self):
        self.first = input().lower()
        self.second = input().lower()

    def process_task(self):
        if self.first == self.second:
            self.result = "0"
        elif self.first > self.second:
            self.result = "1"
        else:
            self.result = "-1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask112ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
