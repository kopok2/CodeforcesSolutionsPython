class CodeforcesTask817ASolution:
    def __init__(self):
        self.result = ''
        self.cords = []
        self.moves = []

    def read_input(self):
        self.cords = [int(x) for x in input().split(" ")]
        self.moves = [int(x) for x in input().split(" ")]

    def process_task(self):
        if (abs(self.cords[0]-self.cords[2]) % self.moves[0]) == 0 and \
                (abs(self.cords[1]-self.cords[3]) % self.moves[1]) == 0:
            if (((abs(self.cords[0]-self.cords[2]) // self.moves[0]) % 2) == 0 and
                    ((abs(self.cords[1]-self.cords[3]) // self.moves[1]) % 2) == 0) or (
                    ((abs(self.cords[0]-self.cords[2]) // self.moves[0]) % 2) == 1 and
                    ((abs(self.cords[1]-self.cords[3]) // self.moves[1]) % 2) == 1):
                self.result = "YES"
            else:
                self.result = "NO"
        else:
            self.result = "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask817ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
