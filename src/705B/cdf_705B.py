class CodeforcesTask705BSolution:
    def __init__(self):
        self.result = ''
        self.cycles = []

    def read_input(self):
        input()
        self.cycles = [int(x) for x in input().split(" ")]

    def process_task(self):
        moves = 0
        for x in range(len(self.cycles)):

            moves += self.cycles[x] - 1
            #for y in range(x + 1):
            #    moves += self.cycles[y] - 1
            print("{0}".format((moves + 1) % 2 + 1))


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask705BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
