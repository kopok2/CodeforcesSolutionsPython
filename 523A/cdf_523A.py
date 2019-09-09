class CodeforcesTask523ASolution:
    def __init__(self):
        self.result = ''
        self.w_h = []
        self.image = []

    def read_input(self):
        self.w_h = [int(x) for x in input().split(" ")]
        for x in range(self.w_h[1]):
            self.image.append(list(input()))

    def process_task(self):
        rotated = [["_" for x in range(self.w_h[1])] for y in range(self.w_h[0])]
        for x in range(self.w_h[1]):
            for y in range(self.w_h[0]):
                rotated[y][x] = self.image[x][y]
        zoomed = [[c + c for c in row] for row in rotated]
        for row in zoomed:
            print("".join(row))
            print("".join(row))


    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask523ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
