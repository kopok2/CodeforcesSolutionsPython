class CodeforcesTask485ASolution:
    def __init__(self):
        self.result = ''
        self.a_m = []

    def read_input(self):
        self.a_m = [int(x) for x in input().split(" ")]

    def process_task(self):
        t = 0
        limit = 10 ** 6
        x, m = self.a_m
        while x % m and t < limit:
            x += x % m
            t += 1
        self.result = "Yes" if t < limit else "No"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask485ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
