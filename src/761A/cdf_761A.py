class CodeforcesTask761ASolution:
    def __init__(self):
        self.result = ''
        self.a_b = []

    def read_input(self):
        self.a_b = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.result = "YES" if abs(self.a_b[0] - self.a_b[1]) <= 1 and sum(self.a_b) else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask761ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
