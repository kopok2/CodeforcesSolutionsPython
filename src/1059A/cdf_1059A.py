class CodeforcesTask1059ASolution:
    def __init__(self):
        self.result = ''
        self.n_l_a = []
        self.customers = []

    def read_input(self):
        self.n_l_a = [int(x) for x in input().split(" ")]
        for x in range(self.n_l_a[0]):
            self.customers.append([int(x) for x in input().split(" ")])

    def process_task(self):
        breaks = 0

        if self.customers:
            breaks += self.customers[0][0] // self.n_l_a[2]
            breaks += (self.n_l_a[1] - self.customers[self.n_l_a[0]-1][0] - self.customers[self.n_l_a[0]-1][1]) // self.n_l_a[2]
            for x in range(len(self.customers)-1):
                breaks += (self.customers[x+1][0] - self.customers[x][0] - self.customers[x][1]) // self.n_l_a[2]
        else:
            breaks += self.n_l_a[1] // self.n_l_a[2]
        self.result = str(breaks)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    Solution = CodeforcesTask1059ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
