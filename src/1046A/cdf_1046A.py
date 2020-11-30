def can_talk(a, b, k, i1, i2, r1, r2):
    if abs(a - b) - r1 <= 0 and abs(a - b) - r2 <= 0:
        if abs(i1 - i2) <= k:
            return True
        else:
            return False
    else:
        return False

class CodeforcesTask1046ASolution:
    def __init__(self):
        self.result = ''
        self.n_k = []
        self.robots = []

    def read_input(self):
        self.n_k = [int(x) for x in input().split(" ")]

    def process_task(self):
        robots = []
        talks = 0
        for x in range(self.n_k[0]):
            robot = [int(y) for y in input().split(" ")]
            for r in robots:
                if can_talk(robot[0], r[0], self.n_k[1], robot[2], r[2], robot[1], r[1]):
                    talks += 1
            robots.append(robot)
        self.result = str(talks)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1046ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
