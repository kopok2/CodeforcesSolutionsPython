class CodeforcesTask606ASolution:
    def __init__(self):
        self.result = ''
        self.a_b_c = []
        self.x_y_z = []

    def read_input(self):
        self.a_b_c = [int(x) for x in input().split(" ")]
        self.x_y_z = [int(x) for x in input().split(" ")]

    def process_task(self):
        remains = [self.a_b_c[x] - self.x_y_z[x] for x in range(3)]
        budget = sum([x // 2 for x in remains if x > 0])
        needed = sum([-x for x in remains if x < 0])
        if budget >= needed:
            self.result = "Yes"
        else:
            self.result = "No"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask606ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
