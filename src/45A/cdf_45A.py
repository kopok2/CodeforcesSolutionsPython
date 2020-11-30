class CodeforcesTask45ASolution:
    def __init__(self):
        self.result = ''
        self.start_month = 0
        self.target_month = 0

    def read_input(self):
        self.start_month = input()
        self.target_month = int(input())

    def process_task(self):
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        current = months.index(self.start_month) + 1
        to_go = (current + self.target_month) % 12
        if not to_go:
            to_go = 12
        self.result = months[to_go - 1]

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask45ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
