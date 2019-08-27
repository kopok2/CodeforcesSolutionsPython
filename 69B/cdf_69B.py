from operator import itemgetter


class CodeforcesTask69BSolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.players = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[1]):
            self.players.append([int(y) for y in input().split(" ")])

    def process_task(self):
        winners = [[] for x in range(self.n_m[0])]
        for x in range(self.n_m[1]):
            for y in range(self.players[x][0], self.players[x][1] + 1):
                winners[y - 1].append((y, self.players[x][2], self.players[x][3]))
        #print(winners)
        profit = 0
        for path in winners:
            if path:
                minima = min([x[1] for x in path])
                real_win = [x for x in path if x[1] == minima]
                real_win.sort(key=itemgetter(0))
                if real_win:
                    profit += real_win[0][2]
        self.result = str(profit)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask69BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
