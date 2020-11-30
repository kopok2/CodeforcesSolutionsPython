class CodeforcesTask287ASolution:
    def __init__(self):
        self.result = ''
        self.square = []

    def read_input(self):
        self.square = [input() for x in range(4)]

    def process_task(self):
        can = False
        for x in range(3):
            for y in range(3):
                b = 0
                for i in range(2):
                    for j in range(2):
                        if self.square[x + i][y + j] == "#":
                            b += 1
                if b == 1 or b == 3 or b == 0 or b == 4:
                    can = True
        self.result = "NO" if not can else "YES"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask287ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
