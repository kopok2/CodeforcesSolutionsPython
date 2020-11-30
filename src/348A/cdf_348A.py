import math
class CodeforcesTask348ASolution:
    def __init__(self):
        self.result = ''
        self.players = 0
        self.games = []

    def read_input(self):
        self.players = int(input())
        self.games = [int(x) for x in input().split(" ")]

    def process_task(self):
        games = math.ceil(sum(self.games) / (self.players - 1))
        if games < max(self.games):
            self.result = str(max(self.games))
        else:
            self.result = str(games)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask348ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
