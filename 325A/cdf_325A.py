def f(l, i):
    return min(l) if i < 2 else max(l)


class CodeforcesTask325ASolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.rectangles = []

    def read_input(self):
        self.n = int(input())
        for _ in range(self.n):
            self.rectangles.append([int(x) for x in input().split(" ")])

    def process_task(self):
        cords = [f([x[i] for x in self.rectangles], i) for i in range(4)]
        fields = [(x[3] - x[1]) * (x[2] - x[0]) for x in self.rectangles]
        ff = sum(fields)
        if ff == (cords[3] - cords[1]) * (cords[2] - cords[0]) and cords[3] - cords[1] == cords[2] - cords[0]:
            self.result = "YES"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask325ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
