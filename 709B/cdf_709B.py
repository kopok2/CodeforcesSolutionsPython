class CodeforcesTask709BSolution:
    def __init__(self):
        self.result = ''
        self.n_a = []
        self.points = []

    def read_input(self):
        self.n_a = [int(x) for x in input().split(" ")]
        self.points = [int(x) for x in input().split(" ")]

    def process_task(self):
        right_points = [x - self.n_a[1] for x in self.points if x >= self.n_a[1]]
        left_points = [self.n_a[1] - x for x in self.points if x < self.n_a[1]]
        right_points.sort()
        left_points.sort()
        if len(right_points) > 0:
            full_right = right_points[-1]
        else:
            full_right = 0
        if len(left_points) > 0:
            full_left = left_points[-1]
        else:
            full_left = 0
        if len(right_points) > 1:
            semi_right = right_points[-2]
        else:
            semi_right = 0
        if len(left_points) > 1:
            semi_left = left_points[-2]
        else:
            semi_left = 0
        variant1 = semi_left * 2 + full_right
        variant2 = semi_right * 2 + full_left
        variant3 = semi_left + full_right * 2
        variant4 = semi_right + full_left * 2
        self.result = str(min(variant1, variant2, variant3, variant4))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask709BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
