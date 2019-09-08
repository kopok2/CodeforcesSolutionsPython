class CodeforcesTask515ASolution:
    def __init__(self):
        self.result = ''
        self.a_b_s = []

    def read_input(self):
        self.a_b_s = [int(x) for x in input().split(" ")]

    def process_task(self):
        min_dist = abs(self.a_b_s[0]) + abs(self.a_b_s[1])
        if self.a_b_s[2] < min_dist:
            self.result = "No"
        else:
            self.result = "Yes" if not (self.a_b_s[2] - min_dist) % 2 else "No"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask515ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
