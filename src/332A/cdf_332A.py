import math


class CodeforcesTask332ASolution:
    def __init__(self):
        self.result = ''
        self.players = 0
        self.game = ''

    def read_input(self):
        self.players = int(input())
        self.game = [x for x in input()]

    def process_task(self):
        for x in range(len(self.game) // self.players + int(math.ceil((len(self.game) % self.players) / self.players))):
            self.game[x * self.players] = "_"
        game = "".join(self.game)
        self.result = str(game.count("bbb_") + game.count("aaa_"))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask332ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
