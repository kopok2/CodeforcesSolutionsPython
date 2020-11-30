class CodeforcesTask390ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.rings = []

    def read_input(self):
        self.n = int(input())
        for x in range(self.n):
            self.rings.append([int(y) for y in input().split(" ")])

    def process_task(self):
        ys = [x[0] for x in self.rings]
        xs = [x[1] for x in self.rings]
        self.result = str(min(len(set(ys)), len(set(xs))))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask390ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
