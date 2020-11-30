class CodeforcesTask323ASolution:
    def __init__(self):
        self.result = ''
        self.k = 0

    def read_input(self):
        self.k = int(input())

    def process_task(self):
        if self.k % 2:
            self.result = "-1"
        elif self.k == 2:
            self.result = "bb\nww\n\nbb\nww"
        else:
            level = "b"
            cube = [[[None for y in range(self.k)] for x in range(self.k)] for z in range(self.k)]
            for z in range(self.k):
                level = "w" if z % 2 else "b"
                for k in range(self.k // 2):
                    # upper
                    for x in range(2 * (k + 1)):
                        cube[z][self.k // 2 - 1 - k][self.k // 2 - 1 - k + x] = level
                    # lower
                    for x in range(2 * (k + 1)):
                        cube[z][self.k // 2 + k][self.k // 2 - 1 - k + x] = level
                    # left
                    for y in range(2 * (k + 1)):
                        cube[z][self.k // 2 - 1 - k + y][self.k // 2 - 1 - k] = level
                    # right
                    for y in range(2 * (k + 1)):
                        cube[z][self.k // 2 - 1 - k + y][self.k // 2 + k] = level
                    level = "w" if level == "b" else "b"

            for layer in cube:
                for row in layer:
                    print("".join(row))
                print(" ")

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask323ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
