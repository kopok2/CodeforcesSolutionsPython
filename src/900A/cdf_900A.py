class CodeforcesTask900ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.points = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.points.append([int(y) for y in input().split(" ")])

    def process_task(self):
        left = 0
        right = 0
        for point in self.points:
            if point[0] < 0:
                left += 1
            else:
                right += 1
        if min(left, right) <= 1:
            self.result = "Yes"
        else:
            self.result = "No"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask900ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
