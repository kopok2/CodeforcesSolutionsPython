from operator import itemgetter


class CodeforcesTask230ASolution:
    def __init__(self):
        self.result = ''
        self.s_n = []
        self.dragons = []

    def read_input(self):
        self.s_n = [int(x) for x in input().split(" ")]
        for y in range(self.s_n[1]):
            self.dragons.append([int(x) for x in input().split(" ")])

    def process_task(self):
        self.dragons.sort(key=itemgetter(0))
        strength = self.s_n[0]
        x = 0
        while x < self.s_n[1] and strength > self.dragons[x][0]:
            strength += self.dragons[x][1]
            x += 1
        self.result = "YES" if x == self.s_n[1] else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask230ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
