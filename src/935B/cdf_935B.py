class CodeforcesTask935BSolution:
    def __init__(self):
        self.result = ''
        self.n = 0
        self.moves = ''

    def read_input(self):
        self.n = int(input())
        self.moves = input()

    def process_task(self):
        x = 0
        y = 0
        coins = 0
        side = ''
        for c in self.moves:
            if c == "R":
                x += 1
            else:
                y += 1
            if x == y:
                side += "0"
            elif x > y:
                side += "2"
            else:
                side += "1"
        coins = side.count("201") + side.count("102")
        self.result = str(coins)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask935BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
