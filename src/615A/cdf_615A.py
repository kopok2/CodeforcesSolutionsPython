class CodeforcesTask615ASolution:
    def __init__(self):
        self.result = ''
        self.n_m = []
        self.b_lamps = []

    def read_input(self):
        self.n_m = [int(x) for x in input().split(" ")]
        for x in range(self.n_m[0]):
            self.b_lamps.append([int(x) for x in input().split(" ")])

    def process_task(self):
        on = [False for x in range(self.n_m[1])]
        for button in self.b_lamps:
            for x in range(1, len(button)):
                on[button[x] - 1] = True
        if False in on:
            self.result = "NO"
        else:
            self.result = "YES"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask615ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
