def intersects(speed, positions, time):
    lmax = -1_000_000_000_000_000_000_000_000_001
    rmin = 1_000_000_000_000_000_000_000_000_001
    for x in range(len(speed)):
        l = positions[x] - time * speed[x]
        r = positions[x] + time * speed[x]
        lmax = max(lmax, l)
        rmin = min(rmin, r)
    return rmin >= lmax - 0.0000001


class CodeforcesTask782BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.positions = []
        self.speeds = []

    def read_input(self):
        self.n = int(input())
        self.positions = [int(x) for x in input().split(" ")]
        self.speeds = [int(x) for x in input().split(" ")]

    def process_task(self):
        l = 0
        r = 1_000_000_000
        while r - l > 0.0000001:
            # print(l, r)
            if intersects(self.speeds, self.positions, r):
                r = l + (r - l) / 2
            else:
                l, r = r, r + (r - l) / 2
        self.result = str(r)


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask782BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
