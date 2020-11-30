class CodeforcesTask263ASolution:
    def __init__(self):
        self.result = ''
        self.matrix = []

    def read_input(self):
        self.matrix = [[int(x) for x in input().split(" ")] for y in range(5)]

    def process_task(self):
        x = 1
        posx = 0
        posy = 0
        for row in self.matrix:
            if 1 in row:
                posy = x
                posx = row.index(1) + 1
            x += 1
        self.result = str(abs(3 - posx) + abs(3 - posy))

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask263ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
