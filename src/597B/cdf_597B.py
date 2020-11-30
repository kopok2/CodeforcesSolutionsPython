from operator import itemgetter


class CodeforcesTask597BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.reservations = []

    def read_input(self):
        self.n = int(input())
        for _ in range(self.n):
            self.reservations.append([int(y) for y in input().split(" ")])

    def process_task(self):
        times = [[x[0] - 1, x[1] - 1, x[1] - x[0]] for x in self.reservations]
        times.sort(key=itemgetter(2))
        taken = [0] * 10**7
        accepted = 0
        for time in times:
            poss = True
            for i in range(time[0], time[1]):
                if taken[i]:
                    poss = False
                    break
            if poss:
                for i in range(time[0], time[1]):
                    taken[i] = 1
                accepted += 1
        self.result = str(accepted)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask597BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
