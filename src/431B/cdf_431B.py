from itertools import permutations


class CodeforcesTask431BSolution:
    def __init__(self):
        self.result = ''
        self.incr = []

    def read_input(self):
        for x in range(5):
            self.incr.append([int(y) for y in input().split(" ")])

    def process_task(self):
        mx = 0
        for st in permutations([x for x in range(5)]):
            cr = 0
            # before
            cr += self.incr[st[0]][st[1]]
            cr += self.incr[st[1]][st[0]]
            cr += self.incr[st[2]][st[3]]
            cr += self.incr[st[3]][st[2]]
            # first in
            cr += self.incr[st[1]][st[2]]
            cr += self.incr[st[2]][st[1]]
            cr += self.incr[st[3]][st[4]]
            cr += self.incr[st[4]][st[3]]
            # second in
            cr += self.incr[st[2]][st[3]]
            cr += self.incr[st[3]][st[2]]
            # third in
            cr += self.incr[st[3]][st[4]]
            cr += self.incr[st[4]][st[3]]
            mx = max(mx, cr)
        self.result = str(mx)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask431BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
