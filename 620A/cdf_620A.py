class CodeforcesTask620ASolution:
    def __init__(self):
        self.result = ''
        self.r_cord = []
        self.d_cord = []

    def read_input(self):
        self.r_cord = [int(x) for x in input().split(" ")]
        self.d_cord = [int(x) for x in input().split(" ")]

    def process_task(self):
        self.result = str(max(abs(self.r_cord[0] - self.d_cord[0]), abs(self.r_cord[1] - self.d_cord[1])))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask620ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
